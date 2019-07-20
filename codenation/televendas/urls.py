router = routers.DefaultRouter()
router.register(r'comissions', ComissionPlanViewSet)

urlpatterns = [
    path('', include(router.urls))
]
