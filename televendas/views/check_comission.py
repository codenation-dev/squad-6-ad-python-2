from rest_framework.decorators import api_view
from televendas.models.sale import Sale


@api_view(['POST'])
def check_comission(request):
    """
    post:
    Check if amount sale is great than avarage of the last five months.
    """
    if isinstance(request.data['seller'], int):
        seller = Seller.objects.get(pk=request.data['seller'])
        sales = Sale.objects.filter(seller_id=seller.id).values_list('amount', flat=True).order_by('-month')[:5]
        if len(sales) > 0:            
            sum = 0.0
            notify = False
            for idx, val in enumerate(sorted(sales), 1):
                sum +=  float(val) * float(idx)
            avg = sum/len(sales)
            minimum_amount = avg - (avg * 10 / 100)
            try:
                if isinstance(request.data['amount'], float):
                    if minimum_amount > request.data['amount']:
                        notify = True
                        try:
                            send_mail(
                                'Notification about sales',
                                'Your sales are below average',
                                'notify@televendas.local',
                                [seller.email],
                                fail_silently=False,
                            )
                        except Exception as e:
                            pass
                    else:
                        notify = False
                else:
                    return Response({'error': 'amount must be float type'}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                pass
            return Response({'notify': notify})
