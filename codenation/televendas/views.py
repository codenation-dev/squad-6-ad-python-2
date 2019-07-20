from rest_framework import status, viewsets
from televendas.serializers import ComissionPlanSerializer
from .models import ComissionPlan

class ComissionPlanViewSet(viewsets.ModelViewSet):
    queryset = ComissionPlan.objects.all()
    serializer_class = ComissionPlanSerializer

