from rest_framework import viewsets
from api_telemetria import models 
from api_telemetria.api import serializers
from drf_yasg.utils import swagger_auto_schema 

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from api_telemetria.api.services import processar_csv_medicoes

from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Sum
from django.db.models import F
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = models.Marca.objects.all()
    serializer_class = serializers.MarcaSerializer
    @swagger_auto_schema(
        operation_description="Retorna Todas as Informações de Marca",
        responses={200: serializers.MarcaSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de Marca",
        responses={201: serializers.MarcaSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de Marca conforme ID informado",
        responses={200: serializers.MarcaSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera a Marca conforme dados passados, para o ID informado",
        responses={200: serializers.MarcaSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Apaga o registro de Marca conforme ID informado",
        responses={200: serializers.MarcaSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class ModeloViewSet(viewsets.ModelViewSet):
    queryset = models.Modelo.objects.all()
    serializer_class = serializers.ModeloSerializer
    @swagger_auto_schema(
        operation_description="Retorna Todas as Informações de Modelo",
        responses={200: serializers.ModeloSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de Modelo",
        responses={201: serializers.ModeloSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de Modelo conforme ID informado",
        responses={200: serializers.ModeloSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o Modelo conforme dados passados, para o ID informado",
        responses={200: serializers.ModeloSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Apaga o registro de Modelo conforme ID informado",
        responses={200: serializers.ModeloSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = models.Veiculo.objects.all()
    serializer_class = serializers.VeiculoSerializer
    @swagger_auto_schema(
        operation_description="Retorna Todas as Informações de Veiculo",
        responses={200: serializers.VeiculoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de Veiculo",
        responses={201: serializers.VeiculoSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de Veiculo conforme ID informado",
        responses={200: serializers.VeiculoSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o Veiculo conforme dados passados, para o ID informado",
        responses={200: serializers.VeiculoSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Apaga o registro de Veiculo conforme ID informado",
        responses={200: serializers.VeiculoSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class UnidadeMedidaViewSet(viewsets.ModelViewSet):
    queryset = models.UnidadeMedida.objects.all()
    serializer_class = serializers.UnidadeMedidaSerializer
    @swagger_auto_schema(
        operation_description="Retorna Todas as Informações de Unidade de Medida",
        responses={200: serializers.UnidadeMedidaSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de Unidade de Medida",
        responses={201: serializers.UnidadeMedidaSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de Unidade de Medida conforme ID informado",
        responses={200: serializers.UnidadeMedidaSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera a Unidade de Medida conforme dados passados, para o ID informado",
        responses={200: serializers.UnidadeMedidaSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Apaga o registro de Unidade de Medida conforme ID informado",
        responses={200: serializers.UnidadeMedidaSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class MedicaoViewSet(viewsets.ModelViewSet):
    queryset = models.Medicao.objects.all()
    serializer_class = serializers.MedicaoSerializer
    @swagger_auto_schema(
        operation_description="Retorna Todas as Informações de Tipos de Medição",
        responses={200: serializers.MedicaoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de tipo de medição",
        responses={201: serializers.MedicaoSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de tipo de medição conforme ID informado",
        responses={200: serializers.MedicaoSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o tipo de medição conforme dados passados, para o ID informado",
        responses={200: serializers.MedicaoSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Apaga o registro de tipo de medição conforme ID informado",
        responses={200: serializers.MedicaoSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class MedicaoVeiculoViewSet(viewsets.ModelViewSet):
    queryset = models.MedicaoVeiculo.objects.all()
    serializer_class = serializers.MedicaoVeiculoSerializer

    @swagger_auto_schema(
        operation_description="Retorna os dados completos das medições dos veículos",
        responses={200: serializers.DadosRelatorioSerializer(many=True)}
    )
    @action(detail=False, methods=['get'])
    def relatorio(self, request):

        dados = models.MedicaoVeiculo.objects.select_related(
            'medicaoid__unidademedida',
            'veiculoid__modeloid',
            'veiculoid__marcaid'
        ).annotate(
            descricao=F('veiculoid__descricao'),
            modelo=F('veiculoid__modeloid__nome'),
            marca=F('veiculoid__marcaid__nome'),
            tipo=F('medicaoid__tipo'),
            simbolo=F('medicaoid__unidademedida__simbolo')
        ).values(
            'id',
            'data',
            'valor',
            'descricao',
            'modelo',
            'marca',
            'tipo',
            'simbolo'
        )

        serializer = serializers.DadosRelatorioSerializer(
            dados,
            many=True
        )

        return Response(serializer.data)
    
class ImportarMedicaoCSVViewSet(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = serializers.UploadCSVSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        arquivo = serializer.validated_data["arquivo"]

        try:
            resultado = processar_csv_medicoes(arquivo)
 
            return Response(
                {
                    "mensagem": "Arquivo processado com sucesso.",
                    "resultado": resultado,
                },
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:
            return Response(
                {
                    "erro": "Falha ao processar o arquivo.",
                    "detalhe": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        

class medicaoVeiculoTempViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MedicaoVeiculoTempSerializer
    queryset = models.MedicaoVeiculoTemp.objects.all()
    
class DadosRelatorioViewSet(viewsets.ViewSet):    
    @swagger_auto_schema(
        operation_description="Retorna os dados completos das medições dos veículos"
    )
    @action(detail=False, methods=['get'])
    def relatorio(self, request):

        medicoes = models.MedicaoVeiculo.objects.select_related(
    'medicao__unidade_medida',
    'veiculo__modelo',
    'veiculo__marca'
    ).annotate(
    descricao=F('veiculo__descricao'),
    modelo=F('veiculo__modelo__nome'),
    marca=F('veiculo__marca__nome'),
    tipo=F('medicao__tipo'),
        ).values(
            'id',
            'data',
            'valor',
            'descricao',
            'modelo',
            'marca',
            'tipo',
        )

        return Response(medicoes)