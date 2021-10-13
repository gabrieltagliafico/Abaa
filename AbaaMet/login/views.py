from typing import ContextManager
from django.shortcuts import render
from django.contrib.auth.views import *

# Create your views here.

class LoginFormView(LoginView):
    template_name = 'login.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['tittle']= 'Iniciar sesion'
        return context