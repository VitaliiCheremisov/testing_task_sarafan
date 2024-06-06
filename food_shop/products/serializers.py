from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Продуктов."""

    class Meta:
        model = Product
        fields = (
            'name',
            'slug',
            'image_small',
            'image_medium',
            'image_lagre'
        )
