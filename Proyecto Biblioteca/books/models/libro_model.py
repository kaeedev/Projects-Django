from django.db import models
from .autor_model import Autor
from .editorial_model import Editorial
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class Libro(models.Model):
    titulo = models.CharField(max_length=300)
    isbn = models.CharField(max_length=13, unique=True)
    fecha_publicacion = models.DateField()
    numero_paginas = models.IntegerField()

    LANG_CHOICES = {
        'ES': 'Español',
        'EN': 'Ingles',
        'IT': 'Italiano'
    }

    idioma = models.CharField(max_length=2, choices=LANG_CHOICES, default='ES')
    descripcion = models.TextField(blank=True, null=True)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, blank=True, null=True)
    autores = models.ManyToManyField(Autor)
    genero = models.CharField(max_length=100, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    is_out_of_stock = models.BooleanField('Esta fuera de stock', default=False)
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = _('Libro')
        verbose_name_plural = _('Libros')