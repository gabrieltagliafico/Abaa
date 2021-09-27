import json
from django.http.response import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView
from general.models import *
from general.forms import *
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.utils.decorators import method_decorator



class ProductoListView(ListView):
    model = Producto
    template_name='productos/productos.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data={}
        try:
            action= request.POST['action']
            if action == 'searchdata':
                data=[]
                for i in Producto.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error']=str(e)
        return JsonResponse(data, safe=False)

    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']='Lista de Productos'
        context['create_url']= reverse_lazy('general:ProductoCreateViewpath')
        context['list_url_prod']= reverse_lazy('general:ProductoListViewpath')
        context['list_url_serv']= reverse_lazy('general:ServicioListViewpath')
        context['entity']= 'Productos'
        return context


class ProductoCreateView(CreateView):
    model=Producto
    form_class= ProductoForm
    template_name='productos/createProduct.html'
    success_url= reverse_lazy('general: ProductoListViewpath')
    
    def post(self, request, *args, **kwargs):
        data={}
        try:
            action= request.POST['action']
            if action == 'add':
                form= ProductoForm(request.POST)
                data= form.save()
            else:
                data['error']='No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error']= str(e)
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']='Creacion de un Producto'
        context['entity']= 'Productos'
        context['list_url_prod']= reverse_lazy('general:ProductoListViewpath')
        context['list_url_serv']= reverse_lazy('general:ServicioListViewpath')
        context['action']='add'
        return context

class ProductoUpdateView(UpdateView):
    model=Producto
    form_class= ProductoForm
    template_name='Productos/createProduct.html'
    success_url= reverse_lazy('general:ProductoListViewpath')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']='Edicion de un Producto'
        context['entity']= 'Productos'
        context['list_url_prod']= reverse_lazy('general:ProductoListViewpath')
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
    