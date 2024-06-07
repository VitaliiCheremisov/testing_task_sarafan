from rest_framework import serializers

from food_shop import constants
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


class ShoppingCartSummarySerializer(serializers.Serializer):
    """Сериализатор для отображения корзины."""
    total_cost = serializers.DecimalField(
        max_digits=constants.MAX_DIGITS,
        decimal_places=constants.DECIMAL_PLACES
    )
    total_amount = serializers.ImageField()
