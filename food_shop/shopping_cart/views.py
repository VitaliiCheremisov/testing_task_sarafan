from rest_framework import mixins, viewsets

from products.models import Product
from .serializers import ShoppingCartSerializer
from .models import ShoppingCart


class ShoppingCartViewSet(viewsets.ModelViewSet):
    """Работа с корзиной."""

    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer

    def perform_create(self, serializer):
        """Метод внесения продукта в корзину."""
        product = Product.objects.get(id=self.kwargs['id'])
        serializer.save(product=product, amount=1)

    def perform_update(self, serializer):
        """Метод изменения количества продуктов в корзине."""
        instance = self.get_object()
        instance.amount = serializer.validated_data.get('amount', instance.amount)
        instance.save()

    def perform_destroy(self, instance):
        """Метод удаления продукта из корзины."""
        instance.delete()
