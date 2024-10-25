from django.urls import path
from . import views 

urlpatterns = [
    path('registrarUser/', views.registrarUsuario, name='registrarUser'),
]
