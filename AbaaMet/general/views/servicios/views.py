
import json
from django.http.response import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView
from general.models import *
from general.forms import *
from django.urls import reverse_lazy

def serviciodef(request):
    Servicios = Servicio.objects.all(),
    context= {'Servicios':Servicios}
    return render(request, 'servicios/servicios.html', context)


class ServicioListView(ListView):
    model = Servicio
    template_name='servicios/servicios.html'

    def post(self, request, *args, **kwargs):
        data={'name': 'william',}
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']='Lista de Servicios'
        context['create_url']= reverse_lazy('general:ServicioCreateViewpath')
        context['list_url']= reverse_lazy('general:ServicioListViewpath')
        context['entity']= 'Servicios'
        return context

class ServicioCreateView(CreateView):
    model=Servicio
    form_class= ServicioForm
    template_name='servicios/create.html'
    success_url= reverse_lazy('general:ServicioListViewpath')
    
    def post(self, request, *args, **kwargs):
        data={}
        try:
            action= request.POST['action']
            if action == 'add':
                form= ServicioForm(request.POST)
                data= form.save()
            else:
                data['error']='No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error']= str(e)
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']='Creacion de un servicio'
        context['entity']= 'Servicios'
        context['list_url']= reverse_lazy('general:ServicioListViewpath')
        context['action']='add'
        return context

class ServicioUpdateView(UpdateView):
    model=Servicio
    form_class= ServicioForm
    template_name='servicios/create.html'
    success_url= reverse_lazy('general:ServicioListViewpath')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']='Edicion de un servicio'
        context['entity']= 'Servicios'
        context['list_url']= reverse_lazy('general:ServicioListViewpath')
        context['action']='edit'
        return context

    def post(self, request, *args, **kwargs):
        data={}
        try:
            action= request.POST['action']
            if action == 'edit':
                form= self.get_form()
                data= form.save()
            else:
                data['error']='No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error']= str(e)
        return JsonResponse(data)
    