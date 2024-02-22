from django.urls import path
from .views import add_to_cart, view_cart, remove_from_cart, checkout, order_confirmation

urlpatterns = [
    path('add_to_cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='cart'),
    path('remove_from_cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('order_confirmation/', order_confirmation, name='order_confirmation'),
]
