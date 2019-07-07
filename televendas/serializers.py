from .models import PlanoComissoes, Venda, Vendedor
from rest_framework import serializers

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = ('id', 'url', 'vendedor', 'valor_vendas', 'valor_comissao', 'mes', 'ano', 'created_at', 'updated_at')
        read_only_fields = ('id', 'valor_comissao', 'created_at', 'updated_at')


 
class VendedorSerializer(serializers.ModelSerializer):
    vendas = VendaSerializer(many=True, read_only=True)
    class Meta:
        model = Vendedor
        fields = ('id','url', 'nome','maior_comissao' , 'cep', 'logradouro', 'numero_casa', 'bairro', 'cidade', 'estado', 'telefone', 'data_nascimento','idade', 'email', 'cpf', 'plano_de_comissao','vendas', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
    
    #Não permite alterar o Plano de Comissão
    def update(self, instance, validated_data):                                                     
        if 'plano_de_comissoes' in validated_data:                                                              
            del validated_data['plano_de_comissoes']                                                            
        return super().update(instance, validated_data)
 
class PlanoComissoesSerializer(serializers.ModelSerializer):
    vendedores = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='vendedor-detail'
    )
    class Meta:
        model = PlanoComissoes
        fields = ('id', 'url', 'porcentagem_menor', 'valor_minimo', 'porcentagem_maior', 'vendedores', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')