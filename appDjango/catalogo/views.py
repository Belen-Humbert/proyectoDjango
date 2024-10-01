from django.shortcuts import render

# Create your views here.
# catalogo/views.py
from catalogo import views  # Asegúrate de que esta línea esté presente


from django.shortcuts import render
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all()  # Obtener todos los productos
    return render(request, 'catalogo/lista_productos.html', {'productos': productos})
