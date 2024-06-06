from rest_framework import serializers

from .models import Category, SubCategory


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Категории."""

    class Meta:
        model = Category
        fields = (
            'name',
            'slug',
            'image'
        )


class SubCategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Подкатегории."""

    class Meta:
        model = SubCategory
        fields = (
            'name',
            'slug',
            'image'
        )
