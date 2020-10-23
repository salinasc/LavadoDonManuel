from django.contrib import admin
from .models import Fotos, Producto, MisVis, Slider

# Register your models here.

class FotoRegis(admin.ModelAdmin):
    list_display = ['num_fot', 'nom_fot', 'des_fot', 'foto']
    search_fields = ['num_fot', 'nom_fot']
    list_per_page = 10

class ProdRegis(admin.ModelAdmin):
    list_display = ['num_pro', 'nom_pro', 'pre_pro', 'sto_pro', 'des_pro']
    search_fields = ['num_pro', 'nom_pro']
    list_per_page = 10

class MisVisRegis(admin.ModelAdmin):
    list_display = ['num_misvis','tit1','txt1','tit2','txt2']
    search_fields = ['num_misvis']
    list_per_page = 10    

class SliderRegis(admin.ModelAdmin):
    list_display = ['IdSlider','Slider']
    search_fields = ['IdSlider']
    list_per_page = 10

admin.site.register(Fotos, FotoRegis)
admin.site.register(Producto, ProdRegis)
admin.site.register(MisVis, MisVisRegis)
admin.site.register(Slider, SliderRegis)