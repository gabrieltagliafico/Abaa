from general.models import Servicio
from general.models import Direccion
from general.models import Sucursal
from django.forms import *
from general.models import Cliente, Empresa
from django import forms


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            "id",
            "nombre_completo",
            "telefono",
            "telefono_ad",
            "email",
            "id_empresa",
        ]


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ["id", "razon_social"]


class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ["id", "rfc", "n_cliente", "id_direccion", "id_empresa"]


class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = [
            "id",
            "num_interior",
            "num_exterior",
            "calle",
            "colonia",
            "pais",
            "referencia",
            "localidad",
            "estado",
            "municipio",
            "codigo_postal",
        ]


class ServicioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["class"] = "form-control"
        self.fields["nombre"].widget.attrs[
            "placeholder"
        ] = "Ingrese el nombre del servicio"
        self.fields["precio"].widget.attrs["placeholder"] = "Indique el precio"
        self.fields["detalle"].widget.attrs["placeholder"] = "Descripcion del servicio"
        self.fields["detalle"].widget.attrs["cols"] = 3
        self.fields["detalle"].widget.attrs["rows"] = 3

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data["error"] = form.errors
        except Exception as e:
            data["error"] = str(e)
        return data

    class Meta:
        model = Servicio
        fields = "__all__"
        labels = {"nombre": "Nombre", "precio": "Precio", "detalle": "Detalle"}
