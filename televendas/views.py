from rest_framework import viewsets
from televendas.serializers import PlanoComissoesSerializer, VendaSerializer, VendedorSerializer
from .models import PlanoComissoes, Venda, Vendedor
from rest_framework.response import Response
from django.db.models import Max

class PlanoComissoesViewSet(viewsets.ModelViewSet):
    queryset = PlanoComissoes.objects.all()
    serializer_class = PlanoComissoesSerializer

class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.annotate(comission=Max('vendas__valor_comissao')).order_by("-comission")
    serializer_class = VendedorSerializer

class VendaViewSet(viewsets.ModelViewSet):    
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

