from django.urls import path
from . import views

urlpatterns = [
    path('bienvenido', views.bienvenido, name='bienvenido'),
    path('nosotros', views.nosotros, name='nosotros'), 
    path('servicios', views.servicios, name='servicios'),
    path('pedidos', views.pedidos, name='pedidos')
]