"""
URL configuration for setup project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from api_telemetria.api import viewsets
from rest_framework import routers, permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="API para telemetria de veiculos agricolas",
        default_version='v1',
        description="Sistema para cadastro e controle por telemetria de frota de veículos agrícolas",
        terms_of_service="https://www.google.com/terms/",
        contact=openapi.Contact(email="contato@ftese.com"),
        license=openapi.License(name="OpenSource"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r'marcas', viewsets.MarcaViewSet, basename='marca')
router.register(r'modelos', viewsets.ModeloViewSet, basename='modelo')
router.register(r'veiculos', viewsets.VeiculoViewSet, basename='veiculo')
router.register(r'unidades_medida', viewsets.UnidadeMedidaViewSet, basename='unidade_medida')
router.register(r'medicoes', viewsets.MedicaoViewSet, basename='medicao')
router.register(r'medicoes_veiculos', viewsets.MedicaoVeiculoViewSet, basename='medicao_veiculo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
    path(
        "medicoes/importar-csv/",
        viewsets.ImportarMedicaoCSVViewSet.as_view(),
        name="importar-medicoes-csv"
    ),
]

urlpatterns += [
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]