from django.shortcuts import render,redirect
from .models import Cliente
# Create your views here.

def inicio_vista(request):
    losclientes=Cliente.objects.all()
    return render(request,"gestionarClientes.html",{"misclientes":losclientes})

def registrarCliente(request):
    id_cliente=request.POST["txtidcliente"]
    Nombres=request.POST["txtnombres"]
    Apellidos=request.POST["txtapellidos"]
    Direccion=request.POST["txtdireccion"]
    Numpasaporte=request.POST["txtnumpasa"]
    Numerotelefono=request.POST["txtnumtel"]
    Correoelectronico=request.POST["txtcorreo"]
    
    guardarcliente=Cliente.objects.create(id_cliente=id_cliente, Nombres=Nombres, Apellidos=Apellidos, Direccion=Direccion, Numpasaporte=Numpasaporte, Numerotelefono=Numerotelefono, Correoelectronico=Correoelectronico)

    return redirect("/")

def seleccionarCliente(request, id_cliente):
    clientes=Cliente.objects.get(id_cliente=id_cliente)
    return render(request,"editarClientes.html",{"misclientes": clientes})

def editarCliente(request):
    id_cliente=request.POST["txtidcliente"]
    Nombres=request.POST["txtnombs"]
    Apellidos=request.POST["txtapelli"]
    Direccion=request.POST["txtdireccion"]
    Numpasaporte=request.POST["txtnumpasa"]
    Numerotelefono=request.POST["txtnumtele"]
    Correoelectronico=request.POST["txtcorreo"]
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    cliente.Nombres=Nombres
    cliente.Apellidos=Apellidos
    cliente.Direccion=Direccion
    cliente.Numpasaporte=Numpasaporte
    cliente.Numerotelefono=Numerotelefono
    cliente.Correoelectronico=Correoelectronico
    cliente.save()
    return redirect("/")

def borrarCliente(request,id_cliente):
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect("/")