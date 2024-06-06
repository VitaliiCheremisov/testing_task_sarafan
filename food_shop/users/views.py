from djoser.views import UserViewSet as DjoserViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CustomUserViewSet(DjoserViewSet):
    """Работа с моделью пользователя."""

    def get_permissions(self):
        """Настройка разрешения."""
        if self.action == 'retrive':
            return [IsAuthenticatedOrReadOnly()]
        return super().get_permissions()
