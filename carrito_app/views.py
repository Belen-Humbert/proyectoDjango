from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, Order, OrderItem
from catalogo_app.models import Product

@login_required
def agregar_al_carrito(request, product_id):
    producto = Product.objects.get(id=product_id)
    carrito, created = Cart.objects.get_or_create(user=request.user)

    # Verificar si el producto ya está en el carrito
    cart_item, created = CartItem.objects.get_or_create(carrito=carrito, producto=producto)
    if not created:
        cart_item.cantidad += 1  # Aumentar la cantidad si ya existe
    cart_item.save()

    return redirect('ver_carrito')

@login_required
def ver_carrito(request):
    carrito = Cart.objects.get(user=request.user)
    return render(request, 'carrito_app/ver_carrito.html', {'carrito': carrito})

@login_required
def crear_orden(request):
    carrito = Cart.objects.get(user=request.user)
    total = sum(item.producto.precio * item.cantidad for item in carrito.items.all())
    
    orden = Order.objects.create(user=request.user, total=total)
    
    for item in carrito.items.all():
        OrderItem.objects.create(order=orden, product=item.producto, cantidad=item.cantidad, precio=item.producto.precio)

    # Limpiar el carrito después de crear la orden
    carrito.items.all().delete()

    return redirect('ver_orden', orden.id)