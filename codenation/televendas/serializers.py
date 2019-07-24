from .models import ComissionPlan, Seller, Sale
from rest_framework import serializers

class ComissionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComissionPlan
        fields = ('__all__')
        read_only_fields = ('id', 'created_at', 'updated_at')



class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'
        


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

