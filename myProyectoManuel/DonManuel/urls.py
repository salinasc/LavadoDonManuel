from django.contrib import admin
from django.urls import path, include
from .views import Index, Contacto, Galeria, InicioSes, Nosotros, Productos, Registro, Sucursales, CerrarSes, AdminProd, Eliminar, Actu, Actuali

urlpatterns = [
    path('', Index, name = 'index'),
    path('Contacto/', Contacto, name = 'conta'),
    path('Galeria/', Galeria, name = 'gale'),
    path('InicioSesion/', InicioSes, name = 'inises'),
    path('Nosotros/', Nosotros, name = 'noso'),
    path('Productos/', Productos, name = 'prod'),
    path('Registro/', Registro, name = 'regi'),
    path('Sucursales/', Sucursales, name = 'sucur'),
    path('CerrarSesion/', CerrarSes, name = 'cerrars'),
    path('AdminProductos/', AdminProd, name = 'adpro'),
    path('Eliminar_Producto/<id>/', Eliminar, name = 'eliprod'),
    path('Actualizar_Producto/<id>/', Actu, name = 'actprod'),
    path('Actuali/', Actuali, name = 'actuali'),
]
