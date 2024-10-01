from django.urls import path
from .views import carrito_view

urlpatterns = [
    path('', carrito_view, name='carrito'),
]
