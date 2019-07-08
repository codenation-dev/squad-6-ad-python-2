from django.urls import include, path
from rest_framework import routers
from .views import PlanoComissoesViewSet, VendaViewSet, VendedorViewSet, VendedorList

router = routers.DefaultRouter()
router.register(r'planos-de-comissoes', PlanoComissoesViewSet)
router.register(r'vendedores', VendedorViewSet)
router.register(r'vendas', VendaViewSet)

urlpatterns = [
    path('vendedores/mes/<int:mes>', VendedorList.as_view()),
    path('', include(router.urls))
]

