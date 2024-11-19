from django.db import models

# Create your models here.


class Cliente(models.Model):
    id_cliente=models.CharField(primary_key=True,max_length=6)
    Nombres=models.CharField(max_length=50)
    Apellidos=models.CharField(max_length=50)
    Direccion=models.CharField(max_length=50)
    Numpasaporte=models.CharField(max_length=50)
    Numerotelefono=models.CharField(max_length=10)
    Correoelectronico=models.CharField(max_length=10)

    def __str__(self) :
        return self.Nombres