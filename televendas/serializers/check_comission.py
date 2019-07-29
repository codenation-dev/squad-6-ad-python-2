from rest_framework import serializers

class CheckComissionSerializer(serializers.Serializer):
    seller = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=8, decimal_places=2)