from rest_framework import status, viewsets
from rest_framework.response import Response

from products.models import Product
from .serializers import ShoppingCartSerializer, ShoppingCartSummarySerializer
from .models import ShoppingCart
from .utils import get_shopping_cart


class ShoppingCartViewSet(viewsets.ModelViewSet):
    """Работа с корзиной."""

    queryset = ShoppingCart.objects.all()

    def get_serializer_class(self):
        """Выбор сериализатора в зависимости от запроса."""
        if self.action == 'list':
            return ShoppingCartSummarySerializer
        return ShoppingCartSerializer

    def perform_create(self, serializer):
        """Метод внесения продукта в корзину."""
        product = Product.objects.get(id=self.kwargs['id'])
        serializer.save(product=product, amount=1)

    def perform_update(self, serializer):
        """Метод изменения количества продуктов в корзине."""
        instance = self.get_object()
        instance.amount = (serializer.validated_data.
                           get('amount', instance.amount))
        instance.save()

    def perform_destroy(self, instance):
        """Метод удаления продукта из корзины."""
        instance.delete()

    def list(self, request, *args, **kwargs):
        """Метод вывода состава корзины."""
        shopping_cart = get_shopping_cart(request.user)
        serializer = self.serializer_class(shopping_cart)
        return Response(serializer.data)

    def clear(self, request, *args, **kwargs):
        """Метод полной очистки корзины."""
        ShoppingCart.objects.filter(user=request.user).delete()
        return Response({'message': 'Корзина очищена'},
                        status=status.HTTP_204_NO_CONTENT)
