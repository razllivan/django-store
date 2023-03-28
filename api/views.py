from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from api.permissions import IsAdminOrReadOnly
from products.models import Product
from products.serializers import ProductSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)
