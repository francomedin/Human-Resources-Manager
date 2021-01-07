from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Departamento(models.Model):
   name =models.CharField('nombre',max_length=50)
   shortname =models.CharField('nombre_corto',max_length=20) 
   anulate=models.BooleanField('anulado',default=False)  
   
   
   def __str__(self):
       return self.name + " " + self.shortname
       