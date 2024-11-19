from django.shortcuts import render,redirect
from .models import Viajes
# Create your views here.

def inicio_vista(request):
    losviajes=Viajes.objects.all()
    return render(request,"gestionarViajes.html",{"misviajes":losviajes})

def registrarViaje(request):
    id_viaje=request.POST["txtidviaje"]
    Origen=request.POST["txtorigen"]
    Destino=request.POST["txtdestino"]
    Horario=request.POST["txthorario"]
    Distancia=request.POST["txtdistancia"]
    Paradas_Continuas=request.POST["txtparadas"]
    Costo=request.POST["txtcosto"]
    
    guardarviaje=Viajes.objects.create(id_viaje=id_viaje, Origen=Origen, Destino=Destino, Horario=Horario, Distancia=Distancia, Paradas_Continuas=Paradas_Continuas, Costo=Costo)

    return redirect("/")

def seleccionarViaje(request, id_viaje):
    viajes=Viajes.objects.get(id_viaje=id_viaje)
    return render(request,"editarViajes.html",{"misviajes": viajes})

def editarViaje(request):
    id_viaje=request.POST["txtidviaje"]
    Origen=request.POST["txtorigen"]
    Destino=request.POST["txtdestino"]
    Horario=request.POST["txthorario"]
    Distancia=request.POST["txtdistancia"]
    Paradas_Continuas=request.POST["txtparadas"]
    Costo=request.POST["txtcosto"]
    viaje=Viajes.objects.get(id_viaje=id_viaje)
    viaje.Origen=Origen
    viaje.Destino=Destino
    viaje.Horario=Horario
    viaje.Distancia=Distancia
    viaje.Paradas_Continuas=Paradas_Continuas
    viaje.Costo=Costo
    viaje.save()
    return redirect("/")

def borrarViaje(request,id_viaje):
    viaje=Viajes.objects.get(id_viaje=id_viaje)
    viaje.delete()
    
    return redirect("/")