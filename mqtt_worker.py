import datetime
import os
import json
import django
import logging
import paho.mqtt.client as mqtt

# Inicializa Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

from django.conf import settings
from api_telemetria.models import MedicaoVeiculo, Veiculo, Medicao

# Logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mqtt_worker")


def on_connect(client, userdata, flags, rc):
    logger.info(f"[MQTT] Conectado com rc={rc}")

    topic = settings.MQTT.get("TOPIC", "planta/sensores/#")
    client.subscribe(topic)
    logger.info(f"[MQTT] Inscrito em {topic}")


def processar_item(data):
    try:
        valor = float(data.get("valor"))
        veiculoid = int(data.get("veiculoid"))
        medicaoid = int(data.get("medicaoid"))
        datae = datetime.datetime.fromisoformat(data.get("data"))

    except Exception as e:
        logger.error(f"[ERRO] Dados inválidos: {data} | erro={e}")
        return None

    # Buscar relações com segurança
    try:
        veiculo = Veiculo.objects.get(id=veiculoid)
    except Veiculo.DoesNotExist:
        logger.warning(f"[WARN] Veiculo {veiculoid} não encontrado")
        return None

    try:
        medicao = Medicao.objects.get(id=medicaoid)
    except Medicao.DoesNotExist:
        logger.warning(f"[WARN] Medicao {medicaoid} não encontrada")
        return None

    return MedicaoVeiculo(
        data=datae,
        veiculo=veiculo,
        medicao=medicao,
        valor=valor,
    )


def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
    except Exception as e:
        logger.error(f"[ERRO] JSON inválido: {e}")
        return

    itens = []

    if isinstance(payload, dict):
        item = processar_item(payload)
        if item:
            itens.append(item)

    elif isinstance(payload, list):
        for obj in payload:
            item = processar_item(obj)
            if item:
                itens.append(item)
    else:
        logger.error("[ERRO] Payload não é dict nem list")
        return

    # Salvar em lote (muito mais rápido)
    if itens:
        MedicaoVeiculo.objects.bulk_create(itens)
        logger.info(f"[MQTT] {len(itens)} registros salvos")


def main():
    mqtt_cfg = settings.MQTT

    client = mqtt.Client()

    if mqtt_cfg.get("USERNAME") and mqtt_cfg.get("PASSWORD"):
        client.username_pw_set(
            mqtt_cfg.get("USERNAME"),
            mqtt_cfg.get("PASSWORD")
        )

    client.on_connect = on_connect
    client.on_message = on_message

    logger.info(f"[MQTT] Conectando em {mqtt_cfg.get('HOST')}:{mqtt_cfg.get('PORT')}")
    client.connect(
        mqtt_cfg.get("HOST"),
        mqtt_cfg.get("PORT"),
        mqtt_cfg.get("KEEPALIVE", 60)
    )

    client.loop_forever()


if __name__ == "__main__":
    main()