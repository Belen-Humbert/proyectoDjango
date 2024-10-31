# proyectoDjango/login_app/urls.py
from django.urls import path 
from .views import login_view, register_view
from django.contrib.auth import views as auth_views
from .forms import CustomPasswordResetForm  # Importa el formulario personalizado

urlpatterns = [
    path('login/', login_view, name='login'),
    path('registro/', register_view, name='registro'),
    path(
        'password_reset/', 
        auth_views.PasswordResetView.as_view(
            form_class=CustomPasswordResetForm,  # Usa el formulario personalizado
            template_name='login_app/password_reset.html'
        ), 
        name='password_reset'
    ),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='login_app/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='login_app/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='login_app/password_reset_complete.html'), name='password_reset_complete'),
]
