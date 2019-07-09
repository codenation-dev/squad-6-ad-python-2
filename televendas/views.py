from rest_framework import viewsets
from rest_framework import generics
from televendas.serializers import ComissionPlanSerializer, SaleSerializer, SellerSerializer
from .models import ComissionPlan, Sale, Seller
from rest_framework.response import Response
from django.db.models import Max


class ComissionPlanViewSet(viewsets.ModelViewSet):
    queryset = ComissionPlan.objects.all()
    serializer_class = ComissionPlanSerializer

class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

class SellerList(generics.ListAPIView):    
    serializer_class = SellerSerializer
    lookup_url_kwarg = "month"

    def get_queryset(self):
        month = self.kwargs.get(self.lookup_url_kwarg)
        sellers = Seller.objects.filter(sales__month=month).annotate(comission=Max('sales__comission')).order_by("-comission")
        return sellers

class SaleViewSet(viewsets.ModelViewSet):    
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
