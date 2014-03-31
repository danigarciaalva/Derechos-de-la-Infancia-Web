# *-* coding: utf-8 *-*
from django.db import models

class Estado(models.Model):
	nombre			= models.CharField(max_length=70, null=False, blank=False)

	def __unicode__(self):
		return self.nombre

class Anio(models.Model):
	anio 			= models.IntegerField(null=False, blank=False)

class Dominio(models.Model):
	nombre			= models.CharField(max_length=500, blank=False, null=False)

class Indicador(models.Model):
	nombre			= models.CharField(max_length=500, blank=False, null=False)
	dominio 		= models.ForeignKey(Dominio, related_name='indicadores')

class Edad(models.Model):
	rango			= models.CharField(max_length=20, null=False, blank=False)

class Valor(models.Model):
	estado 			= models.ForeignKey(Estado, null=True)
	anio 			= models.ForeignKey(Anio, null=True)
	dominio 		= models.ForeignKey(Dominio, null=True)
	indicador 		= models.ForeignKey(Indicador, null=True)
	edad 			= models.ForeignKey(Edad, null=True)
	cantidad		= models.DecimalField(decimal_places=2, max_digits=12)
	CHOICES			= (
		('M', 'Niños'),
		('F', 'Niñas'),
		('A', 'Ambos')
	)
	genero			= models.CharField(max_length=1, choices=CHOICES, null=True, default='A')

