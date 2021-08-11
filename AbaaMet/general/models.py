from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.

class Direccion(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    num_interior= models.IntegerField(null=True)
    num_exterior= models.IntegerField(null=True)
    calle= models.CharField(null=True, max_length=50)
    colonia= models.CharField(null=True, max_length=20)
    pais= models.CharField(null=False,max_length=15)
    referencia= models.CharField(max_length=254, null=True)
    localidad= models.CharField(max_length=30,null=True)
    estado= models.CharField(max_length=20,null=True)
    municipio= models.CharField(max_length=20, null=True)
    codigo_postal= models.PositiveIntegerField(null=False)

class Empresa(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    razon_social = models.CharField(max_length=50)

class Sucursal(models.Model):
    id= models.PositiveIntegerField(primary_key=True)
    id_direccion= models.ForeignKey(Direccion,null=False, blank=False, on_delete= DO_NOTHING)
    id_empresa = models.ForeignKey(Empresa,null=False, blank=False, on_delete=DO_NOTHING)

class Cliente(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    rfc = models.CharField(null=True, max_length=30)
    nombre_completo = models.CharField(null=True,max_length=40)
    telefono = models.IntegerField()
    email= models.EmailField(max_length=254)
    id_empresa= models.ForeignKey(Empresa,null=True, blank=False, on_delete=DO_NOTHING)





class Servicio(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    detalle = models.CharField(max_length=254)











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