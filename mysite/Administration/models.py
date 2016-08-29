from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Proyecto(models.Model):
	nombreProyecto = models.CharField(max_length=50, primary_key=True)
	csvArchive = models.FileField()

	def __str__(self):
		return self.nombreProyecto
