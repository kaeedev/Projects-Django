from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=100)
    biografia = models.TextField()
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    sitio_web = models.URLField(blank=True, null=True)
    premios = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.fecha_nacimiento}"
    
    class Meta:
        verbose_name = _('Autor')
        verbose_name_plural = _('Autores')
