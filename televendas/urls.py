from django.urls import include, path
from rest_framework import routers
from .views.comission_plan import ComissionPlanViewSet

router = routers.DefaultRouter()
router.register(r'comissions', ComissionPlanViewSet)

urlpatterns = [
    path('', include(router.urls))
]
