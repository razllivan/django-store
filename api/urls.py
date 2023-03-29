from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import BasketModelViewSet, CustomAuthToken, ProductModelViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'products', ProductModelViewSet)
router.register(r'baskets', BasketModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token-auth/', CustomAuthToken.as_view()),
]
