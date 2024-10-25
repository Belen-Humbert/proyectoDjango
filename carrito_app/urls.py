from django.urls import path
from .views import agregar_al_carrito, ver_carrito, crear_orden

urlpatterns = [
    path('agregar/<int:product_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('ver/', ver_carrito, name='ver_carrito'),
    path('crear-orden/', crear_orden, name='crear_orden'),
]
