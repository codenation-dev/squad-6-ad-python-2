from django.urls import include, path
from rest_framework import routers
from .views.comission_plan import ComissionPlanViewSet
from rest_framework.documentation import include_docs_urls


router = routers.DefaultRouter()
router.register(r'comissions', ComissionPlanViewSet)

urlpatterns = [
    path('', include_docs_urls(title='Televendas API')),
    path('api/v1/', include(router.urls))

]
