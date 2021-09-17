from general.views.login.views import login
from django.urls import path
from general.views.servicios.views import *

app_name='general'

urlpatterns = [
   path('', login, name='login'),
   path('principal1/', ServicioListView.as_view(), name='ServicioListViewpath'),
   path('principal1/create/', ServicioCreateView.as_view(), name='ServicioCreateViewpath'),
   path('principal1/edit/<int:pk>/', ServicioUpdateView.as_view(), name='ServicioUpdateViewpath'),

]