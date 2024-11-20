from django.shortcuts import render, get_object_or_404
from .models import Product
from .models import Category

def catalogo_view(request):
    productos = Product.objects.all()
    categorias = Category.objects.all()
    return render(request, 'catalogo_app/catalogo.html', {'productos': productos, 'categorias' : categorias})

def poductCat(request, categoria_id):
    categoria = get_object_or_404(Category, id=categoria_id)#Si no se encuentra la categoría con el ID especificado, Django muestra automáticamente una página de error 404.
    productos = Product.objects.filter(categoria=categoria)
    categorias = Category.objects.all()
    return render(request, 'catalogo_app/catalogo.html', {'productos': productos, 'categorias': categorias, 'categoria_seleccionada': categoria})