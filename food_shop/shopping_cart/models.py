from django.contrib.auth import get_user_model
from django.db import models

from food_shop import constants
from products.models import Product

CustomUser = get_user_model()


class ShoppingCart(models.Model):
    """Модель Корзины."""

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Пользователь'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    amount = models.PositiveIntegerField(
        default=constants.AMOUNT_DEFAULT,
        verbose_name='Количество'
    )
    total_price = models.DecimalField(
        max_digits=constants.MAX_DIGITS,
        decimal_places=constants.DECIMAL_PLACES
    )

    def __str__(self):
        return f'{self.product.name} - {self.amount}'

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
