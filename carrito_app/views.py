from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart, CartItem, Order, OrderItem
from catalogo_app.models import Product
from decimal import Decimal

@login_required
def agregar_al_carrito(request, product_id):
    producto = get_object_or_404(Product, id=product_id)
    
    # Verificar si hay stock suficiente
    if producto.stock < 1:
        messages.error(request, "Lo sentimos, no hay stock disponible de este producto.")
        return redirect('catalogo')
        
    carrito, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(
        carrito=carrito,
        producto=producto,
        defaults={'cantidad': 0}
    )
    
    # Verificar que no exceda el stock disponible
    if cart_item.cantidad + 1 <= producto.stock:
        cart_item.cantidad += 1
        cart_item.save()
        messages.success(request, f"{producto.nombre} añadido al carrito.")
    else:
        messages.warning(request, f"No hay suficiente stock para añadir más unidades de {producto.nombre}.")
    
    return redirect('ver_carrito')

@login_required
def ver_carrito(request):
    carrito, created = Cart.objects.get_or_create(user=request.user)
    items = carrito.items.all().select_related('producto')
    
    # Calcular subtotal y total
    subtotal = sum(item.producto.precio * item.cantidad for item in items)
    envio = Decimal('5.99') if subtotal > 0 else Decimal('0')
    total = subtotal + envio
    
    context = {
        'carrito': carrito,
        'items': items,
        'subtotal': subtotal,
        'envio': envio,
        'total': total
    }
    
    return render(request, 'carrito_app/ver_carrito.html', context)

@login_required
def actualizar_cantidad(request, item_id):
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))
        item = get_object_or_404(CartItem, id=item_id, carrito__user=request.user)
        
        if cantidad <= 0:
            item.delete()
            messages.success(request, "Producto eliminado del carrito.")
        elif cantidad <= item.producto.stock:
            item.cantidad = cantidad
            item.save()
            messages.success(request, "Cantidad actualizada.")
        else:
            messages.error(request, "No hay suficiente stock disponible.")
            
    return redirect('ver_carrito')

@login_required
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, carrito__user=request.user)
    item.delete()
    messages.success(request, "Producto eliminado del carrito.")
    return redirect('ver_carrito')

@login_required
def crear_orden(request):
    carrito = get_object_or_404(Cart, user=request.user)
    if not carrito.items.exists():
        messages.error(request, "Tu carrito está vacío.")
        return redirect('ver_carrito')
        
    # Verificar stock antes de crear la orden
    for item in carrito.items.all():
        if item.cantidad > item.producto.stock:
            messages.error(request, f"No hay suficiente stock de {item.producto.nombre}")
            return redirect('ver_carrito')
    
    # Calcular total
    subtotal = sum(item.producto.precio * item.cantidad for item in carrito.items.all())
    envio = Decimal('5.99')
    total = subtotal + envio
    
    # Crear la orden
    orden = Order.objects.create(
        user=request.user,
        total=total,
        status='Pendiente'
    )
    
    # Crear items de la orden y actualizar stock
    for item in carrito.items.all():
        OrderItem.objects.create(
            order=orden,
            product=item.producto,
            cantidad=item.cantidad,
            precio=item.producto.precio
        )

        # No actualizar stock ni vaciar carrito aún
    return render(request, 'carrito_app/compra.html', {'orden': orden})    


# @login_required
# def compra(request, orden_id):
#     orden = get_object_or_404(Order, id=orden_id, user=request.user)

#     if request.method == 'POST':
        #tipo_pago = request.POST.get('tipo_pago')
        #ubicacion = request.POST.get('ubicacion')
        
         #if tipo_pago and ubicacion:
            # Actualizar orden con datos adicionales
         #   orden.tipo_pago = tipo_pago
          #  orden.ubicacion = ubicacion
           # orden.status = 'Completo'
            #orden.save()

            # Actualizar stock y vaciar carrito
    #         for item in orden.orderitem_set.all():
    #             item.product.stock -= item.cantidad
    #             item.product.save()
    #         orden.user.cart.items.all().delete()

    #         return redirect('catalogo')
    # else:
    #         messages.error(request, "Por favor completa todos los campos.")

    # return render(request, 'carrito_app/compra.html', {'orden': orden})

@login_required
def ver_orden(request, orden_id):
    # Obtener la orden actualizada
    orden = get_object_or_404(Order, id=orden_id, user=request.user)
    
    if request.method == 'POST':
        tipo_pago = request.POST.get('tipo_pago')
        ubicacion = request.POST.get('ubicacion')
        
        if tipo_pago and ubicacion:
            # Actualizar orden con datos adicionales
            orden.tipo_pago = tipo_pago
            orden.ubicacion = ubicacion
            orden.status = 'Completo'
            orden.save()


    # Renderizar la orden en la plantilla
    return render(request, 'carrito_app/ver_orden.html', {'orden': orden})    


@login_required
def gestionar_compra(request, orden_id):
    orden = get_object_or_404(Order, id=orden_id, user=request.user)
    if request.method == 'POST':
        accion = request.POST.get('accion')
        if accion == 'finalizar':
            # Lógica para finalizar la compra
            for item in orden.orderitem_set.all():
                item.product.stock -= item.cantidad
                item.product.save()
            orden.user.cart.items.all().delete()

            messages.success(request, "Compra finalizada correctamente.")
            return redirect('catalogo')
        
        elif accion == 'cancelar':
            # Lógica para cancelar la orden
            orden.delete()  # Elimina la orden de la base de datos
            messages.info(request, "Orden cancelada correctamente.")
            return redirect('catalogo')

        else:
            messages.error(request, "Acción no válida.")
            return redirect('catalogo')
