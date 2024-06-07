from rest_framework import serializers

from .models import ShoppingCart


class ShoppingCartSerializer(serializers.ModelSerializer):
    """Сериализатор для Корзины."""

    class Meta:
        model = ShoppingCart
        fields = (
            'user',
            'product',
            'amount',
            'total_price'
        )
