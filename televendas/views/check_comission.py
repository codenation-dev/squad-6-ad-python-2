from rest_framework.generics import GenericAPIView 
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from televendas.models.sale import Sale
from televendas.models.seller import Seller
from televendas.serializers.check_comission import CheckComissionSerializer
from django.core.mail import send_mail


class CheckComission(GenericAPIView):
    serializer_class = CheckComissionSerializer
    """
    post:
    Check if amount sale is great than avarage of the last five months.
    """
    def post(self, request, *args, **kwargs):
        serializer = CheckComissionSerializer(data=request.data)
        if serializer.is_valid():

            seller = get_object_or_404(Seller, pk=request.data['seller'])

            sales = Sale.objects.filter(
                seller_id=seller.pk).values_list(
                'amount', flat=True).order_by('-month')[:5]

            if len(sales) > 0:        

                sum_values = 0.0
                sum_weight = 0
                notify = False
                email_sent = {'message':'', 'sent': False}
                
                for weight, val in enumerate(sorted(sales), 1):
                    sum_values +=  float(val) * float(weight)
                    sum_weight += weight
                avg = float("%0.2f" % (sum_values/sum_weight))
                minimum_amount = float("%0.2f" % (avg - (avg * 10 / 100)))

                if minimum_amount > request.data['amount']:
                    notify = True
                    try:
                        send_mail(
                            'Notificação de Vendas',
                            'Olá você está recebendo esse email porque sua média de vendas está bem abaixo que o esperado.',
                            'notifications@televendas.api',
                            [seller.email],
                            fail_silently=False,
                        ) 
                        email_sent = {'message':'Email enviado com sucesso!', 'sent': True}
                    except Exception as e:
                        email_sent = {'message':'erro ao enviar email. '+str(e), 'sent': False}             
                else:
                    notify = False

                return Response(
                        {
                            'notify': notify, 
                            'avg': avg, 
                            'minimum_amount': minimum_amount, 
                            'email_sent': email_sent
                        }, 
                        status=status.HTTP_200_OK
                    )
            else:
                return Response(
                        {'message': 'Nenhuma venda encontrada para o vendedor: '+seller.name},
                        status=status.HTTP_206_PARTIAL_CONTENT
                    )  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
           
