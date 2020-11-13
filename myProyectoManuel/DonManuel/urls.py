from django.contrib import admin
from django.urls import path, include
from .views import Index, Contactos, Galeria, InicioSes, Nosotros, Registro, Sucursales, CerrarSes, AdminProd, Eliminar, Actu, Actuali, filtro_nombre, filtro_precio, guardar_token #, Productos

urlpatterns = [
    path('', Index, name = 'index'),
    path('Contacto/', Contactos, name = 'conta'),
    path('Galeria/', Galeria, name = 'gale'),
    path('InicioSesion/', InicioSes, name = 'inises'),
    path('Nosotros/', Nosotros, name = 'noso'),
    #path('Productos/', Productos, name = 'prod'),
    path('Registro/', Registro, name = 'regi'),
    path('Sucursales/', Sucursales, name = 'sucur'),
    path('CerrarSesion/', CerrarSes, name = 'cerrars'),
    path('AdminProductos/', AdminProd, name = 'adpro'),
    path('Eliminar_Producto/<id>/', Eliminar, name = 'eliprod'),
    path('Actualizar_Producto/<id>/', Actu, name = 'actprod'),
    path('Actuali/', Actuali, name = 'actuali'),
    path('accounts/login/', InicioSes, name = "acclogin"),
    path('filtro_nombre/', filtro_nombre, name = "filnom"),
    path('filtro_precio/', filtro_precio, name = "filpre"),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('guardar-token/', guardar_token, name="guardar-token"),
]
