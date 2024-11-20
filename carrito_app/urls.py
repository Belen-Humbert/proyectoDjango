from django.urls import path
from . import views

urlpatterns = [
    path('agregar/<int:product_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('ver/', views.ver_carrito, name='ver_carrito'),
    path('actualizar/<int:item_id>/', views.actualizar_cantidad, name='actualizar_cantidad'),
    path('eliminar/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('crear-orden/', views.crear_orden, name='crear_orden'),
]
