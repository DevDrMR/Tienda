from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
#importaciones para manejo de autenticación
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
#importaciones para el manejo de errores
from django.db import IntegrityError


# Home
def home(request):
    return TemplateResponse(request, 'home.html')


####################################################
# CRUD de la clase articulo                        #
####################################################
# Permite al super usuario agregar un nuevo articulo
@staff_member_required
def crear_articulo(request, id=None):
    from catalogo.forms import ArticuloForm
    from catalogo.forms import Articulo

    obj = Articulo.objects.filter(pk=id).first()
    path_img = guarda_path_img(obj)
    form = ArticuloForm(request.POST or None, request.FILES or None, instance=obj)

    if request.method == 'GET':
        parametros = { 'form': form }
        return TemplateResponse(request, 'articulo.html', parametros)
    else:
        if form.is_valid():
            try:
                if len(request.FILES) and not path_img is None:
                    elimina_imagen(path_img)
                form.save()
                return redirect('listadoArticulo')
            except ValueError:
                return render(request, 'articulo.html', {
                    'form': form,
                    'error': 'Error en los datos'
                })

def guarda_path_img(articulo):
    if articulo is None:
        return None
    else:
        return articulo.imagen.path
     
def elimina_imagen(path):
    import os
    if os.path.isfile(path):
            os.remove(path)

# Muestra los productos sin importar si se inició sessión o no
def catalogo(request, modo=None):
    from catalogo.models import Articulo
    parametros = {
        'data': Articulo.objects.all()
    }
    return TemplateResponse(request, 'catalogo.html', parametros)


# Muestra la lista de articulos al super usuario

@staff_member_required
def listado_articulo(request, modo=None):
    from catalogo.models import Articulo
    parametros = {
        'data': Articulo.objects.all()
    }
    return TemplateResponse(request, 'listado_articulo.html', parametros)


# Permite al super usuario eliminar un articulo de la lista
@staff_member_required
def eliminar_articulo(request, id):
    from catalogo.models import Articulo
    try:
        articulo = Articulo.objects.get(pk=id)
        articulo.delete()
        return redirect('listadoArticulo')
    except:
        print("Error al eliminar")
        return redirect('listadoArticulo')


#####################################################
# CRUD de la clase Proveedor                        #
#####################################################
# Permite al super usuario agregar un nuevo proveedor
@staff_member_required
def agrega_proveedor(request, id=None):
    from catalogo.models import Proveedor
    from catalogo.forms import ProveedorForm

    obj = Proveedor.objects.filter(pk=id).first()
    form = ProveedorForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('listadoProveedor')
    
    parametros = {
        'form': form
    }
    return TemplateResponse(request, 'proveedor.html', parametros)


# Muestra la lista de proveedores
@staff_member_required
def mostrar_listado_proveedor(request):
    from catalogo.models import Proveedor
    parametros = {
        'data': Proveedor.objects.all()
    }
    print(parametros)
    return TemplateResponse(request, 'listado_proveedor.html', parametros)


# Permite eliminar a un proveedor junto con los productos
# asociados a él
@staff_member_required
def eliminar_proveedor(request, id):
    from catalogo.models import Proveedor
    obj = Proveedor.objects.filter(pk=id).delete()
    
    return redirect('listadoProveedor')


########################################################
# Views de creacion y autenticación de usuarios        #
########################################################
# View encargada de crear un nuevo usuario
def crear_usuario(request):

    if request.method == 'GET':
        parametros = {'form': UserCreationForm}
        return TemplateResponse(request, 'signup.html', parametros)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password= request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                parametros = {'form': UserCreationForm, 'error': 'El usuario ya existe'}
                return redirect(request, 'signup.html', parametros)
        else:
            parametros = {'form': UserCreationForm, 'error': "Las contraseñas son distintas"}
            return redirect(request, 'signup.html', parametros)
                        

# Se encarga de dar acceso a cada usuario a su cuenta
def iniciar_sesion(request):
    if request.method == 'GET':
        parametros = {'form': AuthenticationForm}
        return TemplateResponse(request, 'signin.html', parametros)
    else:
        user = authenticate(request, username= request.POST['username'], password= request.POST['password'])
        if user is None:
            parametros = {'form': AuthenticationForm, 'error': "Nombre de usuario o contraseña incorrecta"}
            return redirect(request, 'signin.html', parametros)
        else:
            login(request, user)
            return redirect('home')


# Cierra la sesión en las cuentas
def cerrar_sesion(request):
    logout(request)
    return redirect('home')


##########################################################
# Views de Compra                                        #
##########################################################

@login_required
def carrito(request):
    return TemplateResponse(request, 'home.html')


@login_required
def pedidos(request):
    return TemplateResponse(request, 'home.html')