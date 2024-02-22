from django.shortcuts import render, redirect
from .models import CartItem, Order
from .forms import CartItemForm
from product.models import Product


# Create your views here.
def add_to_cart(request, book_id):
    book = Product.objects.get(pk=book_id)

    cart_item, created = CartItem.objects.get_or_create(book=book)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')

def view_cart(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.book.price * item.quantity for item in cart_items)
    subtotal_list = [item.book.price * item.quantity for item in cart_items]

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price, 'subtotal_list': subtotal_list})

def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(pk=cart_item_id)
    cart_item.delete()
    return redirect('cart')

def checkout(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.book.price * item.quantity for item in cart_items)
    subtotal_list = [item.book.price * item.quantity for item in cart_items]

    if request.method == 'POST':
        order = Order.objects.create(total_price=total_price)
        order.items.set(cart_items)
        cart_items.delete()
        return redirect('order_confirmation')

    return render(request, 'checkout.html', {'cart_items': cart_items, 'total_price': total_price, 'subtotal_list': subtotal_list})

def order_confirmation(request):
    orders = Order.objects.all()
    return render(request, 'order_confirmation.html', {'orders': orders})