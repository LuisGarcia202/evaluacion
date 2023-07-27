from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acerca_de/', views.acerca_de, name='acerca_de'),
    path('contacto/', views.contacto, name='contacto'),
]
