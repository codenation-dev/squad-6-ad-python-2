from rest_framework import generics
from .models import Seller
from .serializers import SellerSerializer


# Create your views here.
class MusicSeller(generics.ListCreateAPIView):

    queryset = Seller.objects.all()
    serializer_class = SellerSerializer