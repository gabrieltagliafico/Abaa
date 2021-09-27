from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import EmailField
from django.forms.models import model_to_dict
from django.shortcuts import render

# Create your models here.

class Direccion(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    num_interior= models.IntegerField(null=True,verbose_name='num_interior')
    num_exterior= models.IntegerField(null=True,verbose_name='num_exterior')
    calle= models.CharField(null=True, max_length=50,verbose_name='calle')
    colonia= models.CharField(null=True, max_length=20,verbose_name='colonia')
    pais= models.CharField(null=False,max_length=15,verbose_name='pais')
    referencia= models.CharField(max_length=254, null=True,verbose_name='referencia')
    localidad= models.CharField(max_length=30,null=True,verbose_name='localidad')
    estado= models.CharField(max_length=20,null=True,verbose_name='estado')
    municipio= models.CharField(max_length=20, null=True,verbose_name='municipio')
    codigo_postal= models.PositiveIntegerField(null=False,verbose_name='codigo_postal')
    def __str__(self) -> str:
        return self.localidad
    def toJSON(self):
        item= model_to_dict(self)
        return item

class Empresa(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    razon_social = models.CharField(max_length=50,verbose_name='razon_social')
    def __str__(self):
        return self.razon_social
    def toJSON(self):
        item= model_to_dict(self)
        return item


class Sucursal(models.Model):
    id= models.PositiveIntegerField(primary_key=True)
    rfc = models.CharField(null=True, max_length=30,verbose_name='rfc')
    n_cliente= models.CharField(null=True, max_length=10,verbose_name='n_cliente')
    id_direccion= models.ForeignKey(Direccion,null=True, blank=True, on_delete= DO_NOTHING,verbose_name='direccion')
    id_empresa = models.ForeignKey(Empresa,null=True, blank=True, on_delete=DO_NOTHING,verbose_name='empresa')
    def __str__(self):
        return self.rfc
    def toJSON(self):
        item= model_to_dict(self)
        return item


class Cliente(models.Model):
    id = models.PositiveIntegerField(primary_key=True, verbose_name='id')
    nombre_completo = models.CharField(null=True,max_length=40, verbose_name='nombre')
    telefono = models.CharField(max_length=12, verbose_name='telefono')
    telefono_ad = models.CharField(max_length=12,null=True, verbose_name='telefono_ad')
    email= models.EmailField(max_length=254, verbose_name='email')
    id_sucursal= models.ForeignKey(Sucursal,null=True, blank=True, on_delete=DO_NOTHING, verbose_name='sucursal')
    def __str__(self):
        return self.nombre_completo
    def toJSON(self):
        item= model_to_dict(self)
        return item
    


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50,verbose_name='nombre')
    precio = models.PositiveIntegerField(verbose_name='precio')
    marca = models.CharField(max_length=50,verbose_name='marca')
    modelo = models.CharField(max_length=50,verbose_name='model')
    detalle = models.TextField( verbose_name='detalle')
    activo= models.BooleanField(verbose_name='activo', default=True)
    def __str__(self):
        return self.nombre
    def toJSON(self):
        item= model_to_dict(self)
        return item
    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'
        db_table='g_producto'
        ordering= ['id']

class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50,verbose_name='nombre')
    precio = models.PositiveIntegerField(verbose_name='precio')
    detalle = models.TextField( verbose_name='detalle')
    activo= models.BooleanField(verbose_name='activo', default=True)
    def __str__(self):
        return self.nombre
    def toJSON(self):
        item= model_to_dict(self)
        return item
    class Meta:
        verbose_name='Servicio'
        verbose_name_plural='Servicios'
        db_table='g_servicio'
        ordering= ['id']

class Cargo(models.Model):
    id=models.PositiveIntegerField(primary_key=True, verbose_name='id')
    nombre=models.CharField(max_length=100, verbose_name='cargo')
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name='Cargo'
        verbose_name_plural='Cargos'
        db_table='g_cargo'
        ordering=['id']

class Usuario(models.Model):
    id= models.PositiveIntegerField(primary_key=True, verbose_name='id')
    email= models.EmailField(verbose_name='email')
    cargo= models.ForeignKey(Cargo,null=False, blank=False,on_delete=DO_NOTHING, verbose_name='cargo')
    def __str__(self):
        return self.email
    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'
        db_table='g_usuarios'
        ordering=['id']











class Cotizaciones(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    is_cliente = models.ForeignKey(Cliente,null=False,blank=False, on_delete=models.CASCADE)
    fecha_ini= models.DateField(null=False)
    fecha_fin= models.DateField(null=False)
    comentario = models.CharField(max_length=254)
    subtotal= models.FloatField(null=False)
    viaticos= models.FloatField(null=False)
    descuento = models.IntegerField(null=False)
    status= models.BooleanField(default=True)
    total_sin_iva= models.FloatField(null=False)

class Serv_Cot( models.Model):
    id_servicio= models.ForeignKey(Servicio,null=False, blank=False, on_delete=models.CASCADE)
    id_cotizacion= models.ForeignKey(Cotizaciones,null=False, blank=False, on_delete=models.CASCADE)