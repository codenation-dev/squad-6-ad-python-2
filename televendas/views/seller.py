from rest_framework import status, viewsets
from televendas.serializers.seller import SellerSerializer
from televendas.models.seller import Seller
from rest_framework.decorators import action
from django.db.models import Max
from rest_framework.response import Response


class SellerViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given Seller.

    list:
    Return a list of all the existing Sellers.

    create:
    Create a new Seller instance.
    """
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    @action(detail=False, methods=['get'], url_path='comissions/(?P<month>[^/.]+)',)
    def comissions(self, request, month):
        """
        get:
        Return a list of Sellers ordereds by value of comission on month.
        """
        sellers = Seller.objects.filter(
            sales__month=month).annotate(
                comission=Max('sales__comission')).values(
                    'id', 'name', 'cpf', 'email', 'phone_number', 'comission').order_by(
                        "-comission")
        page = self.paginate_queryset(sellers)
        if page is not None:
            return Response(page)
        return Response(sellers)
