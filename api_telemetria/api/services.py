# Importação de bibliotecas padrão do Python
import csv  # Para leitura de arquivos CSV
import os  # Para manipulação de diretórios e caminhos
import uuid  # Para gerar identificadores únicos
from decimal import Decimal  # Para trabalhar com números decimais com precisão
from datetime import datetime  # Para manipulação de datas

# Importações do Django
from django.conf import settings  # Acessar configurações do projeto (ex: MEDIA_ROOT)
from django.core.files.storage import FileSystemStorage  # Salvar arquivos no sistema
from django.db import transaction, connection  # Controle de transações e execução de SQL

# Importação dos modelos do sistema
from api_telemetria.models import MedicaoVeiculoTemp, Veiculo, Medicao


def executar_procedure_pos_importacao(arquivoid):
    """
    Função responsável por executar uma procedure no banco de dados
    após a importação do arquivo CSV.
    """
    with connection.cursor() as cursor:
        # Executa a procedure chamada "processa_arquivo"
        # passando o identificador do arquivo como parâmetro
        cursor.callproc("processa_arquivo", [arquivoid])


def processar_csv_medicoes(arquivo):
    """
    Função principal que recebe um arquivo CSV,
    valida os dados e insere no banco.
    """

    # Gera um ID único para identificar essa importação
    arquivoid = str(uuid.uuid4())

    # Define a pasta onde o arquivo será salvo
    pasta_destino = os.path.join(settings.MEDIA_ROOT, "importacoes_medicao")

    # Cria a pasta caso ela não exista
    os.makedirs(pasta_destino, exist_ok=True)

    # Define o nome do arquivo com o ID único
    nome_salvo = f"{arquivoid}_{arquivo.name}"

    # Salva o arquivo usando o sistema de storage do Django
    fs = FileSystemStorage(location=pasta_destino)
    nome_arquivo_salvo = fs.save(nome_salvo, arquivo)

    # Caminho completo do arquivo salvo
    caminho_completo = os.path.join(pasta_destino, nome_arquivo_salvo)

    # Inicialização de variáveis de controle
    total_linhas_arquivo = 0  # Total de linhas lidas do CSV
    erros = []  # Lista de erros encontrados
    linhas_para_inserir = []  # Lista de objetos válidos para inserir no banco

    # Cria cache dos dados de veículos e medições (melhora performance)
    veiculos_cache = {v.id: v for v in Veiculo.objects.all()}
    medicoes_cache = {m.id: m for m in Medicao.objects.all()}

    # Abre o arquivo CSV
    with open(caminho_completo, mode="r", encoding="utf-8-sig", newline="") as f:
        
        # Lê o CSV como dicionário (coluna = chave)
        reader = csv.DictReader(f, delimiter=';')

        # Define os campos obrigatórios no CSV
        campos_esperados = {"veiculoid", "medicaoid", "data", "valor"}

        # Verifica se existe cabeçalho
        if not reader.fieldnames:
            raise Exception("O CSV não possui cabeçalho.")

        # Valida se os campos esperados estão presentes
        if not campos_esperados.issubset(set(reader.fieldnames)):
            raise Exception(
                f"Cabeçalho inválido. Esperado: {list(campos_esperados)}. Recebido: {reader.fieldnames}"
            )

        # Percorre cada linha do CSV
        for numero_linha, row in enumerate(reader, start=2):
            total_linhas_arquivo += 1

            try:
                # Converte os IDs para inteiro
                id_veiculo = int(row["veiculoid"])
                id_medicao = int(row["medicaoid"])

                # Busca no cache o veículo correspondente
                veiculo = veiculos_cache.get(id_veiculo)
                if not veiculo:
                    raise Exception(f"Veículo {id_veiculo} não encontrado.")

                # Busca no cache a medição correspondente
                medicao = medicoes_cache.get(id_medicao)
                if not medicao:
                    raise Exception(f"Medição {id_medicao} não encontrada.")

                # Converte a data do formato string para datetime
                data_convertida = datetime.strptime(
                    row["data"].strip(),
                    "%Y-%m-%d %H:%M:%S"
                )

                # Converte o valor para decimal
                valor_convertido = Decimal(row["valor"].strip())

                # Cria um objeto temporário e adiciona na lista
                linhas_para_inserir.append(
                    MedicaoVeiculoTemp(
                        veiculoid=veiculo,
                        medicaoid=medicao,
                        data=data_convertida,
                        valor=valor_convertido,
                        arquivoid=arquivoid
                    )
                )

            except Exception as e:
                # Caso ocorra erro na linha, armazena o erro
                erros.append({
                    "linha": numero_linha,
                    "erro": str(e)
                })

    # Total de linhas válidas
    total_linhas_validas = len(linhas_para_inserir)

    # Inicia uma transação no banco
    with transaction.atomic():

        # Insere os dados em lote (mais eficiente)
        if linhas_para_inserir:
            MedicaoVeiculoTemp.objects.bulk_create(linhas_para_inserir, batch_size=1000)

        # Conta quantas linhas foram realmente inseridas
        total_linhas_importadas = MedicaoVeiculoTemp.objects.filter(
            arquivoid=arquivoid
        ).count()

        # Verifica se o número de linhas bate com o esperado
        quantidades_conferem = total_linhas_validas == total_linhas_importadas

        if quantidades_conferem:
            # Se estiver tudo correto, executa a procedure
            executar_procedure_pos_importacao(arquivoid)
        else:
            # Se houver inconsistência, remove os dados inseridos
            MedicaoVeiculoTemp.objects.filter(arquivoid=arquivoid).delete()

    # Retorna um resumo da importação
    return {
        "arquivoid": arquivoid,
        "arquivo_salvo": nome_arquivo_salvo,
        "caminho": caminho_completo,
        "total_linhas_arquivo": total_linhas_arquivo,
        "total_linhas_importadas": total_linhas_importadas,
        "quantidades_conferem": total_linhas_arquivo == total_linhas_importadas,
        "erros": erros
    }