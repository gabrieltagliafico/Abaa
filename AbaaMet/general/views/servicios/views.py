
import json
from django.http.response import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView
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
        form=ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context= self.get_context_data(**kwargs)
        context['form']=form
        return render(request,self.template_name,context)

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']='Creacion de un servicio'
        context['entity']= 'Servicios'
        context['list_url']= reverse_lazy('general:ServicioListViewpath')
        return context
