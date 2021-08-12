
from django.shortcuts import redirect, render
from general.models import *
from general.forms import *
# Create your views here.
def Clientes(request):
    Clientes = Cliente.objects.all()
    context= {'Clientes':Clientes}
    return render(request,'general/clientes.html', context)

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

