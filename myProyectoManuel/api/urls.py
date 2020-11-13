from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^api/productos/$', views.ProductosViewSet.as_view()),
    url(r'^api/productos_filtro_nombre/(?P<nom_pro>.+)/$', views.ProductosFiltroViewSet.as_view()),
    url(r'^api/productos_filtro_precio/(?P<pre_pro>[0-9]+)/$', views.ProductosFiltroPrecioViewSet.as_view()),
    url(r'^api/contactos/$', views.ContactoViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)