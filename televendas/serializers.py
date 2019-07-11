from .models import ComissionPlan, Sale, Seller
from rest_framework import serializers

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('__all__')
        read_only_fields = ('id', 'comission', 'created_at', 'updated_at')


 
class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = (
            'id',
            'url',
            'name',
            'address',
            'phone',
            'birthday',
            'age',
            'email',
            'cpf',
            'comission_plan',
            'created_at', 
            'updated_at'
        )
        read_only_fields = ('id', 'created_at', 'updated_at')
    
    #Não permite alterar o Plano de Comissão
    def update(self, instance, validated_data):                                                     
        if 'plano_de_comissoes' in validated_data:                                                              
            del validated_data['plano_de_comissoes']                                                            
        return super().update(instance, validated_data)
 
class ComissionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComissionPlan
        fields = ('__all__')
        read_only_fields = ('id', 'created_at', 'updated_at')
