
from django.shortcuts import redirect, render
from general.models import *
from general.forms import *
# Create your views here.
def Clientes(request):
    Clientes = Cliente.objects.all()
    context= {'Clientes':Clientes}
    return render(request,'general/clientes.html', context)

def Empresas(request):
    Empresas = Empresa.objects.all()
    context= {'Empresas':Empresas}
    return render(request,'general/empresas.html', context)

def agregar(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Clientes')
    else:
        form = ClienteForm()
    context= {'form': form}
    return render(request, 'general/agregarCliente.html', context)

def editar(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    if request.method=='POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect("Clientes")
    else:
        form=ClienteForm(instance=cliente)
    context= {"form": form}
    return render(request,"general/editar.html", context)

def editarEmpresa(request, empresa_id):
    empresa = Empresa.objects.get(id=empresa_id)
    if request.method=='POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect("Empresas")
    else:
        form=EmpresaForm(instance=empresa)
    context= {"form": form}
    return render(request,"general/editarEmpresa.html", context)

def agregarEmpresa(request):
    if request.method == "POST":
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Empresas')
    else:
        form = EmpresaForm()
    context= {'form': form}
    return render(request, 'general/agregarEmpresa.html', context)