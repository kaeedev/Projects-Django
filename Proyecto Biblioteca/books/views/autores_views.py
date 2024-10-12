from django.shortcuts import render
from books.forms import  EditorialModelFormCreate
from books.models import Autor
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from books.decorators import user_can_delete_update_autor
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


#ccbv

class AutorListView(ListView):
    model = Autor
    template_name = 'autores/AutorList.html'
    context_object_name = 'autor'


class AutorDetailView(DetailView):
    model = Autor
    template_name = 'autores/AutorDetail.html'
    context_object_name = 'autor'
    

@method_decorator(login_required, name='dispatch')
class AutorCreateView(CreateView):
    model = Autor
    template_name = 'autores/AutorCreate.html'
    success_url = reverse_lazy('autor:list')
    fields = ['nombre', 'apellido', 'fecha_nacimiento', 'nacionalidad', 'biografia', 'email', 'telefono', 'premios', 'sitio_web']
    
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, _('Autor creado con exito.'))
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['nombre'].label = _("nombre")  # Traducción de la etiqueta
        form.fields['apellido'].label = _("apellido")  # Traducción de la etiqueta
        form.fields['fecha_nacimiento'].label = _("fecha_nacimiento")
        form.fields['nacionalidad'].label = _("nacionalidad")
        form.fields['biografia'].label = _("biografia")
        form.fields['email'].label = _("email")
        form.fields['telefono'].label = _("telefono")
        form.fields['premios'].label = _("premios")
        form.fields['sitio_web'].label = _("sitio_web")
        return form

@method_decorator([login_required, user_can_delete_update_autor], name='dispatch')
class AutorUpdateView(UpdateView):
    model = Autor
    template_name = 'autores/AutorUpdate.html'
    success_url = reverse_lazy('autor:list')
    fields = ['nombre', 'apellido', 'fecha_nacimiento', 'nacionalidad', 'biografia', 'email', 'telefono', 'premios', 'sitio_web']
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, _('Autor modificado con exito.'))
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['nombre'].label = _("Nombre")  # Traducción de la etiqueta
        form.fields['apellido'].label = _("Apellido")  # Traducción de la etiqueta
        form.fields['fecha_nacimiento'].label = _("Fecha Nacimiento")
        form.fields['nacionalidad'].label = _("Nacionalidad")
        form.fields['biografia'].label = _("Biografia")
        form.fields['email'].label = _("Email")
        form.fields['telefono'].label = _("Telefono")
        form.fields['premios'].label = _("Premios")
        form.fields['sitio_web'].label = _("Sitio Web")
        return form


@method_decorator([login_required, user_can_delete_update_autor], name='dispatch')
class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'autores/AutorDelete.html'
    success_url = reverse_lazy('autor:list')

    def form_valid(self, form):
        messages.success(self.request, _('Autor borrado con exito.'))
        return super().form_valid(form)