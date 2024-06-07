from .models import ShoppingCart


def get_shopping_cart(user):
    """Формирование и рассчет сумммы и количества товаров."""
    shopping_cart = ShoppingCart.objects.filter(user=user)
    total_cost = sum(item.product.price * item.amount for item in shopping_cart)
    total_amount = sum(item.amount for item in shopping_cart)
    return {
        'total_cost': total_cost,
        'total_amount': total_amount
    }
