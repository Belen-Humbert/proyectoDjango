from django.shortcuts import render
from .models import Product
from .models import Category

def catalogo_view(request):
    productos = Product.objects.all()
    categorias = Category.objects.all()
    return render(request, 'catalogo_app/catalogo.html', {'productos': productos, 'categorias' : categorias})