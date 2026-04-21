from django.urls import path
from . import views 
from .views import logout_usuario,abrir_perfil


urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', logout_usuario, name='logout'),
    path('perfil/', abrir_perfil, name='abrir_perfil'),


]
