from general.views.productos.views import ProductoUpdateView
from general.views.productos.views import ProductoListView
from general.views.login.views import login
from django.urls import path
from general.views.servicios.views import *
from general.views.landing.views import *
from general.views.productos.views import ProductoCreateView
app_name='general'

urlpatterns = [
   path('', login, name='login'),
   path('principal/', landingView , name='LandingPath'),
   path('principal/servicios', ServicioListView.as_view(), name='ServicioListViewpath'),
   path('principal/servicios/create/', ServicioCreateView.as_view(), name='ServicioCreateViewpath'),
   path('principal/servicios/edit/<int:pk>/', ServicioUpdateView.as_view(), name='ServicioUpdateViewpath'),
   path('principal/productos', ProductoListView.as_view(), name='ProductoListViewpath'),
   path('principal/productos/create/', ProductoCreateView.as_view(), name='ProductoCreateViewpath'),
   path('principal/productos/edit/<int:pk>/', ProductoUpdateView.as_view(), name='ProductoUpdateViewpath'),


]