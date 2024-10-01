from django.urls import path
from .views import crud_view

urlpatterns = [
    path('', crud_view, name='crud'),
]
