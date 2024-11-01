from django.urls import path
from . import views 
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('registrarUser/', views.registrarUsuario, name='registrarUser'),
    path('verificarUsuario/', views.verificarUser, name='verificarUsuario'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
    