from django.urls import path
from . import views 

urlpatterns = [
    path('', views.catalogo_view, name='catalogo'),
    path('categoria/<int:categoria_id>/', views.poductCat, name='productCat'),
]