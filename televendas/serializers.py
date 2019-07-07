from .models import PlanoComissoes, Venda, Vendedor
from rest_framework import serializers


class PlanoComissoesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlanoComissoes
        fields = ('id', 'url', 'porcentagem_menor', 'valor_minimo', 'porcentagem_maior', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
 
class VendedorSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model = Vendedor
        fields = ('id','url', 'nome', 'cep', 'logradouro', 'numero_casa', 'bairro', 'cidade', 'estado', 'telefone', 'data_nascimento','idade', 'email', 'cpf', 'plano_de_comissoes', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
    
    #Não permite alterar o Plano de Comissão
    def update(self, instance, validated_data):                                                     
        if 'plano_de_comissoes' in validated_data:                                                              
            del validated_data['plano_de_comissoes']                                                            
        return super().update(instance, validated_data)
      
 
class VendaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Venda
        fields = ('id', 'url', 'vendedor', 'valor_vendas', 'valor_comissao', 'mes', 'ano', 'created_at', 'updated_at')
        read_only_fields = ('id', 'valor_comissao', 'created_at', 'updated_at')
 
