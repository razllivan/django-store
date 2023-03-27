from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import ProductModelViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'products', ProductModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
