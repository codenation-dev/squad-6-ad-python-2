from televendas.models.sale import Sale
from rest_framework import serializers


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('__all__')
        read_only_fields = ('id', 'comission')
        
