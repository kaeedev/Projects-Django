from django.shortcuts import render
from books.forms import  forms
from books.models import Editorial
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from books.decorators import user_can_delete_update_editorial
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.utils.translation import gettext as _


#ccbv

class EditorialListView(ListView):
    model = Editorial
    template_name = 'editoriales/EditorialList.html'
    context_object_name = 'editorial'


class EditorialDetailView(DetailView):
    model = Editorial
    template_name = 'editoriales/EditorialDetail.html'
    context_object_name = 'editorial'
    

@method_decorator(login_required, name='dispatch')
class EditorialCreateView(CreateView):
    model = Editorial
    template_name = 'editoriales/EditorialCreate.html'
    success_url = reverse_lazy('editorial:list')
    fields = ['nombre', 'direccion', 'ciudad', 'estado', 'pais', 'codigo_postal', 'telefono', 'email', 'sitio_web', 'fecha_fundacion']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, _('Editorial creada con exito.'))
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['nombre'].label = _("Nombre")  # Traducción de la etiqueta
        form.fields['ciudad'].label = _("Ciudad")  # Traducción de la etiqueta
        form.fields['estado'].label = _("Estado")
        form.fields['pais'].label = _("Pais")
        form.fields['codigo_postal'].label = _("Codigo Postal")
        form.fields['telefono'].label = _("Telefono")
        form.fields['email'].label = _("Email")
        form.fields['sitio_web'].label = _("Sitio Web")
        form.fields['fecha_fundacion'].label = _("Fecha Fundacion")
        return form
    

@method_decorator([login_required, user_can_delete_update_editorial], name='dispatch')
class EditorialUpdateView(UpdateView):
    model = Editorial
    template_name = 'editoriales/EditorialUpdate.html'
    success_url = reverse_lazy('editorial:list')
    fields = ['nombre', 'direccion', 'ciudad', 'estado', 'pais', 'codigo_postal', 'telefono', 'email', 'sitio_web', 'fecha_fundacion']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, _('Editorial modificada con exito.'))
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['nombre'].label = _("Nombre")  # Traducción de la etiqueta
        form.fields['ciudad'].label = _("Ciudad")  # Traducción de la etiqueta
        form.fields['estado'].label = _("Estado")
        form.fields['pais'].label = _("Pais")
        form.fields['codigo_postal'].label = _("Codigo Postal")
        form.fields['telefono'].label = _("Telefono")
        form.fields['email'].label = _("Email")
        form.fields['sitio_web'].label = _("Sitio Web")
        form.fields['fecha_fundacion'].label = _("Fecha Fundacion")
        return form

@method_decorator([login_required, user_can_delete_update_editorial], name='dispatch')
class EditorialDeleteView(DeleteView):
    model = Editorial
    template_name = 'editoriales/EditorialDelete.html'
    success_url = reverse_lazy('editorial:list')

    def form_valid(self, form):
        messages.success(self.request, _('Editorial borrada con exito.'))
        return super().form_valid(form)