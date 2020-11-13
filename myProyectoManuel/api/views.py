from django.shortcuts import render
from DonManuel.models import Producto, Contacto
from .serializers import ProductosSerializer, ContactoSerializer
from rest_framework import generics

# Create your views here.

class ProductosViewSet(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductosSerializer

class ProductosFiltroViewSet(generics.ListAPIView):
    serializer_class = ProductosSerializer
    def get_queryset(self):
        elnombre = self.kwargs['nom_pro']
        return Producto.objects.filter(nom_pro = elnombre)

class ProductosFiltroPrecioViewSet(generics.ListAPIView):
    serializer_class = ProductosSerializer
    def get_queryset(self):
        precio = self.kwargs['pre_pro']
        return Producto.objects.filter(pre_pro = precio)

class ContactoViewSet(generics.ListCreateAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer