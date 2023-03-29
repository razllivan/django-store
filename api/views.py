from http import HTTPStatus

from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.permissions import IsAdminOrReadOnly
from products.models import Product, Basket
from products.serializers import ProductSerializer, BasketSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAdminOrReadOnly,)


class BasketModelViewSet(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if not user.is_staff:
            return Response({'token': 'Получить токен могут только администраторы'}, status=HTTPStatus.FORBIDDEN)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
