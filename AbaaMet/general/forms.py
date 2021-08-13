from django.forms import fields
from general.models import Cliente,Empresa
from django import forms
class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['id','rfc','nombre_completo','telefono','email','id_empresa']

class EmpresaForm(forms.ModelForm):
    class Meta:
        model= Empresa
        fields= ['id','razon_social']