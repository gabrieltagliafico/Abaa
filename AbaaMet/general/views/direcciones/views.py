
import json
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView
from general.models import *
from general.forms import *
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.utils.decorators import method_decorator



class DireccionesListView(ListView):
    model = Direccion
    template_name='direcciones/direcciones.html'

    
    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data={}
        try:
            action= request.POST['action']
            if action == 'searchdata':
                data=[]
                for i in Direccion.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error']=str(e)
        return JsonResponse(data, safe=False)

    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']='Lista de Direcciones'
        context['list_url_recep']= reverse_lazy('general:RecepcionListViewpath')
        context['create_url']= reverse_lazy('general:DireccionesCreateViewpath')
        context['list_url_cli']= reverse_lazy('general:ClienteListViewpath')
        context['list_url_prod']= reverse_lazy('general:ProductoListViewpath')
        context['list_url_dir']= reverse_lazy('general:DireccionesListViewpath')
        context['list_url_ingre']= reverse_lazy('general:IngresoListViewpath')
        context['list_url_emp']= reverse_lazy('general:EmpresaListViewpath')
        context['list_url_serv']= reverse_lazy('general:ServicioListViewpath')
        context['entity']= 'Direcciones'
        return context

class DireccionesCreateView(CreateView):
    model=Direccion
    form_class= DireccionesForm
    template_name='direcciones/create.html'
    success_url= reverse_lazy('general:DireccionesListViewpath')
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data={}
        try:
            action= request.POST['action']
            if action == 'add':
                form= DireccionesForm(request.POST)
                data= form.save()
            else:
                data['error']='No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error']= str(e)
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']='Creacion de una Direccion'
        context['entity']= 'Direcciones'
        context['list_url']= reverse_lazy('general:DireccionesListViewpath')
        context['list_url_prod']= reverse_lazy('general:ProductoListViewpath')
        context['list_url_recep']= reverse_lazy('general:RecepcionListViewpath')
        context['list_url_cli']= reverse_lazy('general:ClienteListViewpath')
        context['list_url_dir']= reverse_lazy('general:DireccionesListViewpath')
        context['list_url_emp']= reverse_lazy('general:EmpresaListViewpath')
        context['list_url_ingre']= reverse_lazy('general:IngresoListViewpath')
        context['list_url_serv']= reverse_lazy('general:ServicioListViewpath')
        context['action']='add'
        return context

class DireccionesUpdateView(UpdateView):
    model= Direccion
    form_class= DireccionesForm
    template_name='direcciones/create.html'
    success_url= reverse_lazy('general:DireccionesListViewpath')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']='Edicion de una Direccion'
        context['entity']= 'Direcciones'
        context['list_url']= reverse_lazy('general:DireccionesListViewpath')
        context['list_url_cli']= reverse_lazy('general:ClienteListViewpath')
        context['list_url_prod']= reverse_lazy('general:ProductoListViewpath')
        context['list_url_recep']= reverse_lazy('general:RecepcionListViewpath')
        context['list_url_dir']= reverse_lazy('general:DireccionesListViewpath')
        context['list_url_emp']= reverse_lazy('general:EmpresaListViewpath')
        context['list_url_ingre']= reverse_lazy('general:IngresoListViewpath')
        context['list_url_serv']= reverse_lazy('general:ServicioListViewpath')
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
    