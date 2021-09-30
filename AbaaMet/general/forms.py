
from django.forms import *
from general.models import *
from django import forms


class DireccionesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["class"] = "form-control"
        self.fields["pais"].widget.attrs[
            "placeholder"
        ] = "Ingrese el pais"
        self.fields["estado"].widget.attrs["placeholder"] = "Indique el estado"
        self.fields["municipio"].widget.attrs["placeholder"] = "Indique un municipio"
        self.fields["localidad"].widget.attrs["placeholder"] = "Indique su localidad"
        self.fields["referencia"].widget.attrs["placeholder"] = "Diga un lugar de referencia"
        self.fields["colonia"].widget.attrs["placeholder"] = "Indique su colonia"
        self.fields["calle"].widget.attrs["placeholder"] = "Diga su calle"
        self.fields["num_interior"].widget.attrs["placeholder"] = "Indique su numero interior"
        self.fields["num_exterior"].widget.attrs["placeholder"] = "Indique su numero exterior"
        self.fields["codigo_postal"].widget.attrs["placeholder"] = "Indique su codigo postal"
        self.fields["codigo_postal"].widget.attrs["cols"] = 5
        self.fields["codigo_postal"].widget.attrs["rows"] = 5

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
        model = Direccion
        fields = "__all__"
        labels = {"pais": "Pais", "estado": "Estado","municipio": "Municipio","localidad": "Localidad", "referencia": "Referencia", "colonia": "Colonia", "calle": "Calle", "num_interior": "Numero interior", "num_exterior": "Numero exterior", "codigo_postal": "Codigo Postal"}


class ClienteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["class"] = "form-control"
        self.fields["nombre_completo"].widget.attrs[
            "placeholder"
        ] = "Ingrese el nombre del Cliente"
        self.fields["telefono"].widget.attrs["placeholder"] = "Indique el telefono"
        self.fields["telefono_ad"].widget.attrs["placeholder"] = "Indique un telefono adicional"
        self.fields["email"].widget.attrs["placeholder"] = "Indique el email"
        self.fields["id_sucursal"].widget.attrs["placeholder"] = "Seleccione la sucursal a la cual pertenece"
        self.fields["id_sucursal"].widget.attrs["cols"] = 5
        self.fields["id_sucursal"].widget.attrs["rows"] = 5

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
        model = Cliente
        fields = "__all__"
        labels = {"nombre_completo": "Nombre Completo", "telefono": "Telefono","telefono_ad": "Telefono adicional","email": "Email", "id_sucursal": "Sucursal"}


class ProductoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["class"] = "form-control"
        self.fields["nombre"].widget.attrs[
            "placeholder"
        ] = "Ingrese el nombre del servicio"
        self.fields["precio"].widget.attrs["placeholder"] = "Indique el precio"
        self.fields["marca"].widget.attrs["placeholder"] = "Indique la marca"
        self.fields["modelo"].widget.attrs["placeholder"] = "Indique el modelo"
        self.fields["detalle"].widget.attrs["placeholder"] = "Descripcion del producto"
        self.fields["detalle"].widget.attrs["cols"] = 5
        self.fields["detalle"].widget.attrs["rows"] = 5

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
        model = Producto
        fields = "__all__"
        labels = {"nombre": "Nombre", "precio": "Precio","marca": "Marca","modelo": "Modelo", "detalle": "Detalle"}

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


class SucursalForm(ModelForm):
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

class EmpresaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["class"] = "form-control"
        self.fields["razon_social"].widget.attrs[
            "placeholder"
        ] = "Ingrese el nombre de la empresa"
        self.fields["razon_social"].widget.attrs["cols"] = 3
        self.fields["razon_social"].widget.attrs["rows"] = 3

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
        model = Empresa
        fields = "__all__"
        labels = {"razon_social": "Razon social"}
