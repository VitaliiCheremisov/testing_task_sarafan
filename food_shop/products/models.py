from django.db import models

from food_shop import constants
from categories.models import SubCategory


class Product(models.Model):
    """Модель продуктов."""
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=constants.MAX_PRODUCT_NAME_LENGTH,
        verbose_name='Название подкатегории'
    )
    slug = models.SlugField(
        max_length=constants.MAX_CATEGORY_SLUG_LENGTH,
        verbose_name='Слаг'
    )
    image_small = models.ImageField(
        upload_to='media/products/small',
        verbose_name='Маленькое изображение'
    )
    image_medium = models.ImageField(
        upload_to='media/products/medium',
        verbose_name='Среднее изображение'
    )
    image_large = models.ImageField(
        upload_to='media/products/large',
        verbose_name='Большое изображение'
    )
    price = models.DecimalField(
        max_digits=constants.MAX_DIGITS,
        decimal_places=constants.DECIMAL_PLACES,
        verbose_name='Цена'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
