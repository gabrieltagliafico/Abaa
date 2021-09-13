from general.views.login.views import login
from django.urls import path
from general.views.servicios.views import *

app_name='general'

urlpatterns = [
   path('', login, name='login'),
   path('principal/', serviciodef ,name='Serviciodef'),
   path('principal1/', ServicioListView.as_view(), name='ServicioListView')
]
""" ServicioListView.as_view() """