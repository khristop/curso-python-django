from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TipoArticulo(models.Model):
    nombre= models.CharField(max_length = 20)
    descrpcion = models.CharField(max_length = 100)
    
    def __unicode__(self):
        return self.nombre

class Articulo(models.Model):
    
    codigo = models.CharField(primary_key=True, max_length = 5)
    nombre = models.CharField(max_length = 100)
    descripcion = models.CharField(max_length= 250)
    observaciones = models.CharField(max_length= 200)
    tipo = models.ForeignKey(TipoArticulo)
    
    def __unicode__(self):
        return "%s - %s" % (self.codigo,self.nombre)
    
class Estudiante(models.Model):
    carnet = models.CharField(primary_key=True, max_length= 10)
    nombre= models.CharField(max_length = 100)
    
    def __unicode__(self):
        return self.nombre
    
class DetallePrestamo(models.Model):
    
    prestamo_id = models.AutoField(primary_key= True)
    fecha = models.DateTimeField()
    motivo = models.CharField(max_length = 100)
    estado = models.BooleanField( default= False)
    usuario = models.ForeignKey(Estudiante)
    articulo= models.ForeignKey(Articulo)
    
    class Meta:
        unique_together = (('articulo', 'usuario'),)
        
    def __unicode__(self):
        return "%s - %s" % (self.articulo,self.usuario)