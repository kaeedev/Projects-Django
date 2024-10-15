from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from thumbnails.fields import ImageField


# Create your models here.
class Post(models.Model):
    title = models.CharField(
        _('Título'),
        max_length=200
    )
    content = RichTextField(
        _('contenido'),
    )
    author = models.CharField(
        _('Autor'),
        max_length=100
    )
    created_at = models.DateTimeField(
        _('Fecha de creación'),
        default=timezone.now
    )

    show_home = models.BooleanField(
        _('Mostrar en la home'),
        default=False
    )

    blog_image = ImageField(
        _("Portada del curso"),
        upload_to="post/images/",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Publicacion')
        verbose_name_plural = _('Publicaciones')