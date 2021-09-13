import json
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from general.models import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


def serviciodef(request):
    if request.method == "POST" and request.is_ajax():
        value =  json.loads( request.POST['info'] )
        nombre = value[0]['value']
        Precio = value[1]['value']
        detalle = value[2]['value']
        guardar = Servicio(nombre=nombre, Precio=Precio, detalle=detalle)
        guardar.save()
    return JsonResponse(value, safe=False)


class ServicioListView(ListView):
    model = Servicio
    template_name='servicios/servicios.html'


    def post(self, request, *args, **kwargs):
        data={'name': 'william',}
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']='Lista de Servicios'
        return context
    