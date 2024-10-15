from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Contact(models.Model):
    nombre = models.CharField(
        _('Nombre'),
        max_length=50
    )
    email = models.EmailField(
        _('Email')
    )
    comentario = models.TextField(
        _('Comentario que ha dejado en la web')
    )
    created_at = models.DateTimeField(
        _('Fecha de creacion'),
        default=timezone.now
    )
    contactado = models.BooleanField(
        _('¿Se ha contactado con él?'),
        default=False
    )

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = _('Contacto')
        verbose_name_plural = _('Contactos')