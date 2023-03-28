from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import CustomAuthToken
from api.views import ProductModelViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'products', ProductModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token-auth/', CustomAuthToken.as_view()),
]
