from rest_framework import status, viewsets
from televendas.serializers.seller import SellerSerializer
from televendas.models.seller import Seller


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
