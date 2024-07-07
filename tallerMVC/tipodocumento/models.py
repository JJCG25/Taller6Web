from django.db import models

class td(models.Model):
    id = models.AutoField(primary_key=True)
    nombre= models.CharField(max_length = 30)
    descripcion= models.CharField(max_length = 500) 
    
    def __str__(self):
        return self.nombre


# Create your models here.
