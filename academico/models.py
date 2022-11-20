from django.db import models

# Create your models here.

class curso(models.Model):
    Nombre = models.CharField(max_length=40)
    cedula = models.CharField(max_length=40)
    curso = models.CharField(max_length=40)
    estado = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)   

    def __str__(self):
        return self.Nombre


 