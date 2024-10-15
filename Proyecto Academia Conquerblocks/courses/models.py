from django.db import models
from django.utils import timezone
from thumbnails.fields import ImageField
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Course(models.Model):
    title = models.CharField(
        _('Título del curso'),
        max_length=200
    )
    content = RichTextField(
        _('Contenido del curso'),
    )
    call_link = models.URLField(
        _('Enlace de llamada')
    )
    created_at = models.DateTimeField(
        _('Fecha y hora de creación'),
        default=timezone.now
    )
    show_home = models.BooleanField(
        _('Mostrar en la home'),
        default=False
    )
    toc = models.FileField(
        _("Temario"),
        upload_to="courses/toc/",
        null=True,
        blank=True
    )
    course_image = ImageField(
        _("Portada del curso"),
        upload_to="courses/images/",
        null=True,
        blank=True
    )


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Curso')
        verbose_name_plural = _('Cursos')