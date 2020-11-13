from rest_framework import serializers
from DonManuel.models import Producto, Contacto

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ["num_pro","nom_pro","pre_pro","des_pro","sto_pro"]

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ["num_con","nom_con","ape_con","asu_con","tco_con","msg_con"]


        
    