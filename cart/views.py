from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from store.models import Product
from .cart import Cart
from .forms import CartAddProductForm

def cart_detail(request):
    """Страница корзины"""
    cart = Cart(request)
    
    # Обновление количества через POST
    if request.method == 'POST':
        for item in cart:
            quantity_key = f'quantity_{item["product"].id}'
            if quantity_key in request.POST:
                new_quantity = int(request.POST[quantity_key])
                if new_quantity > 0:
                    cart.add(item['product'], quantity=new_quantity, override_quantity=True)
                else:
                    cart.remove(item['product'])
        
        messages.success(request, 'Корзина обновлена')
        return redirect('cart_detail')
    
    return render(request, 'cart/detail.html', {'cart': cart})

@require_POST
def cart_add(request, product_id):
    """Добавление товара в корзину"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            override_quantity=cd['override']
        )
        messages.success(request, f'✅ {product.name} добавлен в корзину')
    
    return redirect(request.META.get('HTTP_REFERER', 'product_list'))

@require_POST
def cart_remove(request, product_id):
    """Удаление товара из корзины"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, f'❌ {product.name} удалён из корзины')
    return redirect('cart_detail')

def cart_clear(request):
    """Очистка корзины"""
    cart = Cart(request)
    cart.clear()
    messages.success(request, '🗑️ Корзина очищена')
    return redirect('product_list')
