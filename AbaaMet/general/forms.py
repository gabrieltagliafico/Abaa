from django.forms import fields
from general.models import Cliente
from django import forms
class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['id','rfc','nombre_completo','telefono','email','id_empresa']
