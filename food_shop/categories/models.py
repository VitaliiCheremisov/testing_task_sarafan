from django.db import models

from food_shop import constants


class Category(models.Model):
    """Модель категории."""
    name = models.CharField(
        max_length=constants.MAX_CATEGORY_NAME_LENGTH,
        verbose_name='Название категории'
    )
    slug = models.SlugField(
        max_length=constants.MAX_CATEGORY_SLUG_LENGTH,
        unique=True,
        verbose_name='Слаг'
    )
    image = models.ImageField(
        upload_to='media/categories',
        verbose_name='Изображение'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    """Модель подкатегории."""
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories'
    )
    name = models.CharField(
        max_length=constants.MAX_CATEGORY_NAME_LENGTH,
        verbose_name='Название подкатегории'
    )
    slug = models.CharField(
        max_length=constants.MAX_CATEGORY_NAME_LENGTH,
        verbose_name='Слаг'
    )
    image = models.ImageField(
        upload_to='media/subcategories'
    )

    def __str__(self):
        return f'{self.category} - {self.name}'

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
