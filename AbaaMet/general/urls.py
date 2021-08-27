from general import views
from django.urls import path

urlpatterns = [
    path("",views.Clientes, name="Clientes"),
    path("agregarCliente/", views.agregar, name="agregarCliente"),
    path("agregarEmpresa/", views.agregarEmpresa, name="agregarEmpresa"),
    path("editar/<int:cliente_id>/", views.editar, name="editar"),
    path("editarEmpresa/<int:empresa_id>/", views.editarEmpresa, name="editarEmpresa"),
    path("sucursales/", views.MostrarSucursales, name="Sucursales"),
    path("empresas/", views.Empresas, name="Empresas"),
    path("direcciones/", views.mostrarDireccion, name="Direcciones"),
    path("agregarDireccion/", views.agregarDireccion, name="agregarDireccion"),
    path("agregarSucursal/", views.agregarSucursal, name="agregarSucursal"),
    path("editarSucursal/<int:sucursal_id>/", views.editarSucursal, name="editarSucursal"),
    path("editarDireccion/<int:direccion_id>/", views.editarDireccion, name="editarDireccion"),
    ]