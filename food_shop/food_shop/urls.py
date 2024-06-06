from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from categories.views import CategoryViewSet

router_v1 = DefaultRouter()
router_v1.register('categories', CategoryViewSet, basename='categories')

api_patterns = [
    path('', include(router_v1.urls)),
    path('auth', include('djoser.urls.authtoken')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include(api_patterns))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
