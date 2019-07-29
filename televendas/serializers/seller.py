from televendas.models.seller import Seller 
from rest_framework import serializers


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = (
            'name',
            'address',
            'phone_number',
            'birthday',
            'age',
            'email',
            'cpf',
            'comission_plan',
        )
        read_only_fields = ('id', 'age')
