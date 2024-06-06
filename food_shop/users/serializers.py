from django.contrib.auth import get_user_model

from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework.serializers import ValidationError

from food_shop.settings import DISALLOWED_USERNAMES

CustomUser = get_user_model()


class CustomUserSerializer(UserSerializer):
    """Сериализатор для модели пользователя."""

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
        )


class CustomUserCreateSerializer(UserCreateSerializer):
    """Сериализатор для создания пользователя."""
    model = CustomUser
    fields = (
        'email',
        'id',
        'username',
        'first_name',
        'last_name',
    )

    def validate_username(self, value):
        """Проверка на запрещенный username."""
        if value.lower() in DISALLOWED_USERNAMES:
            raise ValidationError('Запрещеный username.')
        return value
