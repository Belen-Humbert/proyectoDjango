from django.shortcuts import render
from .models import Product

def catalogo_view(request):
    productos = Product.objects.all()
    return render(request, 'catalogo_app/catalogo.html', {'productos': productos})