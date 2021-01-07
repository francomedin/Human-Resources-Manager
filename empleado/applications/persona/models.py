from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField("Habilidad", max_length=50)
    
    class meta:
        verbose_name="Habilidad"
        verbose_name_plural="Habilidades del empleado"
        
    def __str__(self):
        return str(self.id) + "-" + self.habilidad

class Empleado(models.Model):
    TIPO_TRABAJO=(
        ('0','Contador'),
        ('1','Administrador'),
        ('2','Economista'),
        ('3','Otro')
    )
    
    
    first_name = models.CharField('nombre', max_length=50)
    last_name = models.CharField('apellido', max_length=50)
    full_name=models.CharField('nombre_completo',max_length=101, blank=True)
    job = models.CharField('trabajo', max_length=1, choices=TIPO_TRABAJO)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades=models.ManyToManyField(Habilidades)
    
    
    def __str__(self):
        return self.first_name + " " + self.last_name
