from django.urls import path, include
from rest_framework import routers
from api.views import ProductListAPIView

app_name = 'api'

urlpatterns = [
    path('product-list/', ProductListAPIView.as_view(), name='product-list'),
]
