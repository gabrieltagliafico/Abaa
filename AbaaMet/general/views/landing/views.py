
from typing import ContextManager
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView

from general.models import *


class LandingListView(ListView):
    model=Usuario
    template_name='landing/landing.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']='Principal'
        context['create_url']= reverse_lazy('general:ProductoCreateViewpath')
        context['list_url']= reverse_lazy('general:ProductoListViewpath')
        context['list_url_prod']= reverse_lazy('general:ProductoListViewpath')
        context['list_url_cli']= reverse_lazy('general:ClienteListViewpath')
        context['list_url_dir']= reverse_lazy('general:DireccionesListViewpath')
        context['list_url_emp']= reverse_lazy('general:EmpresaListViewpath')
        context['list_url_serv']= reverse_lazy('general:ServicioListViewpath')
        context['entity']= 'Home'
        return context
