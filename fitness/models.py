from django.db import models

# Create your models here.

class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
    genero     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)


class Datos(models.Model):
    rut              = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    id_genero        = models.ForeignKey('Genero', on_delete=models.CASCADE, db_column='idGenero')  
    telefono         = models.CharField(max_length=45)
    peso             = models.FloatField()  # Corregido de floatfield() a FloatField()
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  
    activo           = models.IntegerField()
  
    def __str__(self):
        return str(self.nombre) + " " + str(self.apellido_paterno)

    class Meta:      
        ordering = ['rut']


class VidaSaludable(models.Model):
    vegetal_favorito = models.CharField(max_length=100)
    peso = models.FloatField()  # Aquí se corrige el error
    ejercicio_favorito = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.vegetal_favorito} - {self.ejercicio_favorito}"
