from django.urls import path 
from .views import login_view, register_view, password_reset_view

urlpatterns = [
    path('', login_view, name='login'),
    path('registro/', register_view, name='registro'),
    path('password_reset/', password_reset_view, name='password_reset'),
]
