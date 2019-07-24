from rest_framework import status, viewsets
from televendas.serializers.comission_plan import ComissionPlanSerializer
from televendas.models.comission_plan import ComissionPlan

class ComissionPlanViewSet(viewsets.ModelViewSet):
    queryset = ComissionPlan.objects.all()
    serializer_class = ComissionPlanSerializer
