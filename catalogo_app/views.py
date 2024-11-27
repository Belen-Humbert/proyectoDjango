from django.shortcuts import render, get_object_or_404
from .models import Product
from .models import Category
from django.core.paginator import Paginator

def catalogo_view(request):
    productos = Product.objects.all()
    categorias = Category.objects.all()

    # Para filtrar por precio
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if min_price:
        productos = productos.filter(precio__gte=min_price)
    if max_price:
        productos = productos.filter(precio__lte=max_price)

    # Paginación
    paginator = Paginator(productos, 12)
    page_number = request.GET.get('page')
    productos_paginated = paginator.get_page(page_number)

    return render(request, 'catalogo_app/catalogo.html', {
        'productos': productos_paginated,
        'categorias': categorias,
        'min_price': min_price,
        'max_price': max_price,
    })

def poductCat(request, categoria_id):
    categoria = get_object_or_404(Category, id=categoria_id)#Si no se encuentra la categoría con el ID especificado, Django muestra automáticamente una página de error 404.
    productos = Product.objects.filter(categoria=categoria)
    categorias = Category.objects.all()
    return render(request, 'catalogo_app/catalogo.html', {'productos': productos, 'categorias': categorias, 'categoria_seleccionada': categoria})