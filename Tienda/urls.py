"""
URL configuration for Tienda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from catalogo import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('usuario/crear', views.crear_usuario, name="crearUsuario"),
    path('usuario/entrar', views.iniciar_sesion, name="iniciarSesion"),
    path('usuario/salir', views.cerrar_sesion, name="cerrarSesion"),
    path('catalogo/', views.catalogo, name="catalogo"),
    path('carrito/', views.carrito, name="carrito"),
    path('pedidos/', views.pedidos, name="pedidos"),
    path('articulo/crear/', views.crear_articulo, name="articulo"),
    path('articulo/editar/<int:id>', views.crear_articulo, name="editarArticulo"),
    path('articulo/eliminar/<int:id>', views.eliminar_articulo, name="eliminarArticulo"),
    path('articulo/listado/', views.listado_articulo, name="listadoArticulo"),
    path('proveedor/crear/', views.agrega_proveedor, name="proveedor"),
    path('proveedor/editar/<int:id>', views.agrega_proveedor, name="editarProveedor"),
    path('proveedor/listado/', views.mostrar_listado_proveedor, name="listadoProveedor"),
    path('proveedor/eliminar/<int:id>', views.eliminar_proveedor, name="eliminarProveedor"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)