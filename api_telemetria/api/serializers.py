from rest_framework import serializers
from telemetria import models


class MarcaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Marca
        fields = '__all__'


class ModeloSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Modelo
        fields = '__all__'


class VeiculoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Veiculo
        fields = '__all__'


class MedicaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Medicao
        fields = '__all__'


class UnidadeMedidaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UnidadeMedida
        fields = '__all__'


class MedicaoVeiculoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MedicaoVeiculo
        fields = '__all__'


class MedicaoVeiculoSerializerTemp(serializers.ModelSerializer):

    class Meta:
        model = models.MedicaoVeiculoTemp
        fields = '__all__'


class DadosRelatorioSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    data = serializers.DateTimeField()
    descricao = serializers.CharField()
    modelo = serializers.CharField()
    marca = serializers.CharField()
    tipo = serializers.CharField()
    valor = serializers.FloatField()


class UpdateCsvStatusSerializer(serializers.Serializer):

    arquivoid = serializers.IntegerField(
        help_text='Identificador do arquivo processado'
    )

    def validate_arquivoid(self, value):

        if not value:
            raise serializers.ValidationError(
                "O campo 'arquivoid' é obrigatório."
            )

        return value