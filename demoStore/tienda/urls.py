from django.urls import path

from . import views

app_name= 'tienda'

urlpatterns = [
    path('', views.index,  name='index'),
    path('registro',views.registro, name='registro'),
    path('login', views.loginUsuario, name='login'),
]