from django.contrib import admin
from .models import ShoppingCart

admin.site.empty_value_display = '-пусто-'


@admin.register(ShoppingCart)
class ShoppingCart(admin.ModelAdmin):
    list_display = ('user', 'product')
    search_fields = ('user',)
    list_filter = ('user',)
