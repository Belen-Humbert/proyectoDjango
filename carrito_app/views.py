from django.shortcuts import render

def carrito_view(request):
    return render(request, 'carrito_app/carrito.html')
