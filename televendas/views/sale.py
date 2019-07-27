from rest_framework import status, viewsets
from televendas.serializers.sale import SaleSerializer
from televendas.models.sale import Sale
 
class SaleViewSet(viewsets.ModelViewSet):    
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer