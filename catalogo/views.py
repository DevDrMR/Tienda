from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
#importaciones para manejo de autenticación
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#importaciones para el manejo de errores
from django.db import IntegrityError


# Create your views here.

#Home
def home(request):
    return TemplateResponse(request, 'home.html')


#Mostrar catalogo
def catalogo(request):
    return TemplateResponse(request, 'home.html')


#Views enfocadas en la creacion y autenticación de usuarios

#View encargada de crear un nuevo usuario
def signup(request):

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
                        

#View encargada de dar acceso a cada usuario a su cuenta
def singin(request):
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

#View encargada de cerrar sesión en las cuentas
def singout(request):
    logout(request)
    return redirect('home')


@login_required
def carrito(request):
    return TemplateResponse(request, 'home')


@login_required
def pedidos(request):
    return TemplateResponse(request, 'home')