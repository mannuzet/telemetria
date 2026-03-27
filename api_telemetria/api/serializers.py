from rest_framework import serializers
from api_telemetria import models 

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marca
        fields = '__all__'
        extra_kwargs = {
          'id': {'help_text': 'Identificador da marca.'},
          'nome': {'help_text': 'Nome da marca do veículo.'},
}

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modelo
        fields = '__all__'
        extra_kwargs = {
         'id': {'help_text': 'Identificador do modelo.'},
         'nome': {'help_text': 'Nome do modelo do veículo.'},
}

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Veiculo
        fields = '__all__'
        extra_kwargs = {
         'id': {'help_text': 'Identificador do veículo.'},
         'descricao': {'help_text': 'Descrição do veículo.'},
         'marca': {'help_text': 'Identificador da marca. Buscar no Get da API Marca.'},
         'modelo': {'help_text': 'Identificador do modelo. Buscar no Get da API Modelo.'},
         'ano': {'help_text': 'Ano de fabricação do veículo.'},
         'horimetro': {'help_text': 'Valor atual do horímetro do veículo.'},
}

class UnidadeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UnidadeMedida
        fields = '__all__'
        extra_kwargs = {
         'id': {'help_text': 'Identificador da unidade de medida.'},
         'nome': {'help_text': 'Nome da unidade de medida (ex: °C, bar, litros).'},
}

class MedicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Medicao
        fields = '__all__'
        extra_kwargs = {
         'id': {'help_text': 'Identificador do tipo de medição.'},
         'tipo': {'help_text': 'Tipo da medição (TEMP, PRESS, COMB).'},
         'unidade_medida': {'help_text': 'Identificador da unidade de medida. Buscar no Get da API UnidadeMedida.'},
}

class MedicaoVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicaoVeiculo
        fields = '__all__'
        extra_kwargs = {
         'id': {'help_text': 'Identificador da Medição veiculo'},
         'veiculoid': {'help_text': 'Identificador do veiculo. Buscar no Get da Api veiculo'},
         'medicaoid': {'help_text': 'Identificador do tipo de medição. Buscar no Get da API Medicao'},
         'data': {'help_text': 'Data e hora da medição realizada, essa informação deve vir da automação'},
         'valor': {'help_text': 'Valor medido na automação.'}
}
        
        