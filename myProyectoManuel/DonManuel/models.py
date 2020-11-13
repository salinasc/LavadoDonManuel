from django.db import models

# Create your models here.

class Fotos(models.Model):
    num_fot = models.AutoField(primary_key = True)
    nom_fot = models.CharField(max_length = 40)
    des_fot = models.TextField()
    foto = models.ImageField(upload_to = 'fotos', null = True)

    def __str__(self):
        return self.nom_fot

class Producto(models.Model):
    num_pro = models.AutoField(primary_key = True)
    nom_pro = models.CharField(max_length = 120)
    pre_pro = models.IntegerField()
    sto_pro = models.IntegerField()
    des_pro = models.TextField()

    def __str__(self):
        return self.nom_pro

class MisVis(models.Model):
    num_misvis = models.AutoField(primary_key = True)
    tit1 = models.CharField(max_length = 100)
    txt1 = models.TextField()
    tit2 = models.CharField(max_length = 100)
    txt2 = models.TextField()

class Slider(models.Model):
    IdSlider = models.CharField(max_length = 120)
    Slider = models.ImageField(upload_to = 'slider', null = True)

    def __str__(self):
        return self.IdSlider

class Contacto(models.Model):
    num_con = models.AutoField(primary_key = True)
    nom_con = models.CharField(max_length = 50)
    ape_con = models.CharField(max_length = 50)
    asu_con = models.CharField(max_length = 50)
    tco_con = models.CharField(max_length = 10)
    msg_con = models.TextField(max_length = 200)

    def __str__(self):
        return self.nom_con