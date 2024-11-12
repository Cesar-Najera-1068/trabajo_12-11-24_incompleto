from django.db import models

# Create your models here.


class Viajes(models.Model):
    id_viaje=models.CharField(primary_key=True,max_length=6)
    Origen=models.CharField(max_length=50)
    Destino=models.CharField(max_length=50)
    Horario=models.CharField(max_length=50)
    Distancia=models.CharField(max_length=50)
    Paradas_Continuas=models.CharField(max_length=10)
    Costo=models.CharField(max_length=10)

    def __str__(self) :
        return self.Destino
