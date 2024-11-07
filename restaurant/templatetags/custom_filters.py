from django import template
from ..models import CartItem

register = template.Library()

@register.filter
def get_item(cart_items, item):
    """Retrieve the cart item corresponding to the given menu item."""
    try:
        cart_item = cart_items.get(menu_item=item)
        return cart_item
    except CartItem.DoesNotExist:
        return None
