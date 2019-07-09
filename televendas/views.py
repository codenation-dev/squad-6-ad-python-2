from rest_framework import viewsets
from rest_framework import generics
from televendas.serializers import PlanoComissoesSerializer, VendaSerializer, VendedorSerializer
from .models import PlanoComissoes, Venda, Vendedor
from rest_framework.response import Response
from django.db.models import Max


class PlanoComissoesViewSet(viewsets.ModelViewSet):
    queryset = PlanoComissoes.objects.all()
    serializer_class = PlanoComissoesSerializer

class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

class VendedorList(generics.ListAPIView):    
    serializer_class = VendedorSerializer
    lookup_url_kwarg = "mes"

    def get_queryset(self):
        mes = self.kwargs.get(self.lookup_url_kwarg)
        vendedores = Vendedor.objects.filter(vendas__mes=mes).annotate(comissao=Max('vendas__valor_comissao')).order_by("-comissao")
        return vendedores

class VendaViewSet(viewsets.ModelViewSet):    
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
