from general.models import Direccion
from general.models import Sucursal
from django.forms import fields
from general.models import Cliente,Empresa
from django import forms

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['id','nombre_completo','telefono','telefono_ad','email','id_empresa']

class EmpresaForm(forms.ModelForm):
    class Meta:
        model= Empresa
        fields= ['id','razon_social']

class SucursalForm(forms.ModelForm):
    class Meta:
        model= Sucursal
        fields=['id','rfc','n_cliente','id_direccion','id_empresa']

class DireccionForm(forms.ModelForm):
    class Meta:
        model=Direccion
        fields=['id','num_interior','num_exterior','calle','colonia','pais','referencia','localidad','estado','municipio','codigo_postal']