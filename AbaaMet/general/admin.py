from general.models import Cliente, Cotizaciones, Direccion, Serv_Cot, Servicio
from django.contrib import admin

# Register your models here.

admin.site.register(Cotizaciones)
admin.site.register(Serv_Cot)
admin.site.register(Servicio)
admin.site.register(Direccion)
admin.site.register(Cliente)

