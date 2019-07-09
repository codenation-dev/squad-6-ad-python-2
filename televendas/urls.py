from django.urls import include, path
from rest_framework import routers
from .views import ComissionPlanViewSet, SellerViewSet, SaleViewSet, SellerList

router = routers.DefaultRouter()
router.register(r'comissions', ComissionPlanViewSet)
router.register(r'sellers', SellerViewSet)
router.register(r'sales', SaleViewSet)

urlpatterns = [
    path('seller/month/<int:month>', SellerList.as_view()),
    path('', include(router.urls))
]

