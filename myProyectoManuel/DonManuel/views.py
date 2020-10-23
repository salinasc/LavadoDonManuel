from django.shortcuts import render
from .models import Producto, Fotos, MisVis, Slider
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def Index(request):
    slider = Slider.objects.all()
    return render(request, 'web/Index.html', {'slider':slider})

def Contacto(request):
    return render(request, 'web/Contacto.html')

def Galeria(request):
    fotos = Fotos.objects.all()
    return render(request, 'web/Galeria.html', {'lista_fotos':fotos})

def InicioSes(request):
    if request.POST:
        use = request.POST.get("txtusu") 
        pas = request.POST.get("txtpass")
        
        us = authenticate(request, username = use , password = pas)

        if us is not None and us.is_active:
            login(request, us)
            slider = Slider.objects.all()
            return render(request, 'web/Index.html', {'usuario':us,'slider':slider})
        else:
            return render(request, 'web/InicioSesion.html', {'msg':'Usuario o contraseña incorrectos'})

    return render(request, 'web/InicioSesion.html')

def CerrarSes(request):
    logout(request)
    slider = Slider.objects.all()
    return render(request, 'web/Index.html', {'slider':slider})

def Nosotros(request):
    textos = MisVis.objects.all()
    return render(request, 'web/Nosotros.html', {'text':textos})

@login_required(login_url = '/InicioSesion/')
@permission_required('DonManuel.add_producto', login_url='/InicioSesion/')
def Productos(request):
    if request.POST:
        accion = request.POST.get("accion")

        if accion == "Registrar":
            nom = request.POST.get("txtNombre")
            pre = request.POST.get("txtvalor")
            des = request.POST.get("txtDescripcion")
            sto = request.POST.get("txtstock")

            producto = Producto(
                nom_pro = nom,
                pre_pro = pre,
                sto_pro = sto,
                des_pro = des
            )

            producto.save()
            return render(request, 'web/Productos.html',{'msg':'Producto registrado'})

        if accion == "Eliminar":
            try:
                prod = Producto.objects.get(nom_pro = nom)
                prod.delete()
                mensaje = "Producto eliminado"
            except:
                mensaje = "Producto no encontrado"
            return render(request, 'web/Productos.html',{'msg':mensaje})

        if accion == "Actualizar":
            nom = request.POST.get("txtNombre")
            pre = request.POST.get("txtvalor")
            des = request.POST.get("txtDescripcion")
            sto = request.POST.get("txtstock")

            try:
                prod = Producto.objects.get(nom_pro = nom)
                prod.nom_pro = nom
                prod.pre_pro = pre
                prod.des_pro = des
                prod.sto_pro = sto

                prod.save()
                mensaje = "Producto actualizado"
            except:
                mensaje = "Producto no encontrado"   

            return render(request, 'web/Productos.html',{'msg':mensaje})


    return render(request, 'web/Productos.html')

def Registro(request):
    if request.POST:
        # rut = request.POST.get("txtRut")
        nom = request.POST.get("txtNombre")
        ape = request.POST.get("txtApellidos")
        ema = request.POST.get("txtEmail")
        # fec = request.POST.get("txtFechaN")
        usu = request.POST.get("txtUser")
        con1 = request.POST.get("txtPass")
        con2 = request.POST.get("txtPass2")

        try:
            u = User.objects.get(username = usu)
            return render(request, 'web/Registro.html',{'msg':'Usuario existe'})
        except:

            try:
                u = User.objects.get(email = ema)
                return render(request, 'web/Registro.html',{'msg':'Correo ya registrado'})
            except:
                if con1 != con2:
                    return render(request, 'web/Registro.html',{'msg':'Las contraseñas no coinciden'})

                u = User()
                u.first_name = nom
                u.last_name = ape
                u.email = ema
                u.username = usu
                u.set_password(con1)

                u.save()            
                us = authenticate(request, username = usu , password = con1)
                login(request, us)
                slider = Slider.objects.all()
                return render(request, 'web/Index.html', {'slider':slider})
              
    return render(request, 'web/Registro.html')

def Sucursales(request):
    return render(request, 'web/Sucursales.html')

@login_required(login_url = '/InicioSesion/')
@permission_required('DonManuel.add_producto', login_url='/InicioSesion/')
def AdminProd(request):
    poduc = Producto.objects.all()
    
    if request.POST:
        accion = request.POST.get("accion")

        if accion == "Registrar":
            nom = request.POST.get("txtNombre")
            pre = request.POST.get("txtvalor")
            des = request.POST.get("txtDescripcion")
            sto = request.POST.get("txtstock")

            producto = Producto(
                nom_pro = nom,
                pre_pro = pre,
                sto_pro = sto,
                des_pro = des
            )

            producto.save()
            mensaje = "Producto registrado"
            return render(request, 'web/AdminProductos.html',{'msg':mensaje,'productos':poduc})

        if accion == "Eliminar":
            #pid = request.POST.get("txtid")
            nom = request.POST.get("txtNom")    

            try:
                prod = Producto.objects.get(nom_pro = nom)
                prod.delete()
                mensaje = "Producto eliminado"
            except:
                mensaje = "Producto no encontrado"
            return render(request, 'web/AdminProductos.html',{'msg':mensaje,'productos':poduc})

    return render(request, 'web/AdminProductos.html',{'productos':poduc})

def Eliminar(request, id):
    try:
        prod = Producto.objects.get(num_pro = id)
        prod.delete()
    except:
        mensaje = "Producto no encontrado"

    poduc = Producto.objects.all()
    return render(request, 'web/AdminProductos.html',{'productos':poduc})

def Actu(request,id):
    try:
        prod = Producto.objects.get(num_pro = id)
        poduc = Producto.objects.all()
        return render(request, 'web/Actualizar_Producto.html',{'productos':poduc,'prod':prod})
    except:
        mensaje = 'Producto no encontrado'
    return render(request, 'web/AdminProductos.html',{'msg':mensaje,'productos':poduc})

def Actuali(request):
    if request.POST:
        nom = request.POST.get("txtNombre")
        pre = request.POST.get("txtvalor")
        des = request.POST.get("txtDescripcion")
        sto = request.POST.get("txtstock")
        
        try:
            prod = Producto.objects.get(nom_pro = nom)
            prod.nom_pro = nom
            prod.pre_pro = pre
            prod.des_pro = des
            prod.sto_pro = sto

            prod.save()
            mensaje = "Producto actualizado"
        except:
            mensaje = "Producto no encontrado"
        poduc = Producto.objects.all()   
        return render(request, 'web/AdminProductos.html',{'msg':mensaje,'productos':poduc})