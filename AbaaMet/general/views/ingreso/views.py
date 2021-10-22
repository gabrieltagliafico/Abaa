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

class IngresoListView(ListView):
    model = Ingreso
    template_name='ingreso/ingreso.html'

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
                ingresos= Ingreso.objects.all()
                recpciones = Recepcion.objects.all()
                for r in ingresos:
                    n_i= r.n_recepcion
                    print('esto es n_i',n_i)
                    for i in recpciones:
                        print('Entre a recepciones',i)
                        if (n_i == i):
                            print('Entre al if',i.cliente)
                            cliente= i.cliente
                            print(r.n_recepcion)
                    data.append(r.toJSON())
                    # data.append(i.cliente.nombre_completo)
                print(data)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error']=str(e)
        return JsonResponse(data, safe=False)

    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']='Lista de Ingresos'
        context['create_url']= reverse_lazy('general:RecepcionCreateViewpath')
        context['list_url_cli']= reverse_lazy('general:ClienteListViewpath')
        context['list_url_dir']= reverse_lazy('general:DireccionesListViewpath')
        context['list_url_emp']= reverse_lazy('general:EmpresaListViewpath')
        context['list_url_prod']= reverse_lazy('general:ProductoListViewpath')
        context['list_url_serv']= reverse_lazy('general:ServicioListViewpath')
        context['list_url_recep']= reverse_lazy('general:RecepcionListViewpath')
        context['list_url_ingre']= reverse_lazy('general:IngresoListViewpath')
        context['entity']= 'Ingreso'
        return context
