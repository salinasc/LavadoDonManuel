from django.test import TestCase
import unittest 
from .models import Producto
from django.contrib.auth.models import User

class TestProducto(unittest.TestCase):

    def agregar_p(self):
        ap = Producto(
            nom = "Cera automotriz", 
            pre = 5500, 
            des = "Acabado brillante, como nuevo ",
            sto = 6
		)

        valor = 0

        try:
            ap.save()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)

    def listar_p(self):
        lp = Producto.objects.all()
        self.assertInstance(lp,Producto) 

class TestUsuario(unittest.TestCase):

    def agregar_u(self):
        au =  User(
            nom="Cristian",
            ape="Valderrama",
            ema="Cristian.vs@gmail.com",
            usu="CristianVS",
            con1="0236"
        )

        valor = 0

        try:
            au.save()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)

    def listar_u(self):
        lu = User.objects.all()
        self.assertInstance(lu,User)

class TestEliminar(unittest.TestCase):

    def elim_prod(self):
        valor = 0

        try:
            prod = Producto.objects.get(num_pro = 1)
            prod.delete()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)
    
    def listar_p(self):
        lp = Producto.objects.all()
        self.assertInstance(lp,Producto)

if __name__ == "__main__":
	unittest.main() 