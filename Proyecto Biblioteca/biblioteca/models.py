from django.db import models
from tabnanny import verbose
from django.utils import timezone
from django.utils.translation import gettext as _

# Create your models here.
class Contact(models.Model):
    nombre = models.CharField(
        max_length=50,
        verbose_name='Nombre'
    )
    email = models.EmailField(
        verbose_name = 'Email'
    )
    comentario = models.TextField(
        verbose_name= 'Comentario que ha dejado en la web'
    )
    created_at = models.DateTimeField(
        verbose_name='Fecha y hora de creacion',
        default = timezone.now
    )
    contactado = models.BooleanField(
        verbose_name='¿Se ha contactado con el?',
        default= False
    )

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')