from televendas.models.comission_plan import ComissionPlan
from rest_framework import serializers


class ComissionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComissionPlan
        fields = ('__all__')
        read_only_fields = ('id', 'created_at', 'updated_at')
