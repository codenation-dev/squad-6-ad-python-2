from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from televendas.models.sale import Sale
from televendas.models.seller import Seller
from televendas.serializers.check_comission import CheckComissionSerializer

class CheckComission(APIView):
    """
    post:
    Check if amount sale is great than avarage of the last five months.
    """
    def post(self, request, format=None):
        serializer = CheckComissionSerializer(data=request.data)
        if serializer.is_valid():
            seller = get_object_or_404(Seller, pk=request.data['seller'])
            sales = Sale.objects.filter(
                seller_id=seller.pk).values_list(
                    'amount', flat=True).order_by('-month')[:5]
            if len(sales) > 0:            
                sum = 0.0
                notify = False
                for idx, val in enumerate(sorted(sales), 1):
                    sum +=  float(val) * float(idx)
                avg = sum/len(sales)
                minimum_amount = avg - (avg * 10 / 100)
                if minimum_amount > request.data['amount']:
                    notify = True    
                    # Chamar aqui, a função que envia o email aqui                        
                else:
                    notify = False
                return Response({'notify': notify}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
           
