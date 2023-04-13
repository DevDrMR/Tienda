from django import forms
from catalogo.models import Articulo, Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model =  Proveedor
        fields = '__all__'

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'