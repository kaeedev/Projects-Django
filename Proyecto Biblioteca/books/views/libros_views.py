from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from books.models import Libro
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from books.decorators import user_can_delete_update_libro
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.utils.translation import gettext as _


class LibroListView(ListView):
    model = Libro
    template_name = 'libros/LibroList.html'
    context_object_name = 'libro'


@method_decorator(login_required, name='dispatch')
class LibroCreateView(CreateView):
    model = Libro
    fields = ['titulo', 'isbn', 'fecha_publicacion', 'numero_paginas', 'idioma']
    template_name = 'libros/LibroCreate.html'
    success_url = reverse_lazy('libro:list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, _('Libro creado con exito.'))
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['titulo'].label = _("Titulo")  # Traducción de la etiqueta
        form.fields['isbn'].label = _("ISBN")  # Traducción de la etiqueta
        form.fields['fecha_publicacion'].label = _("Fecha Publicacion")
        form.fields['numero_paginas'].label = _("Numero Paginas")
        form.fields['idioma'].label = _("Idioma")
        return form


@method_decorator([login_required, user_can_delete_update_libro], name='dispatch')
class LibroUpdateView(UpdateView):
    model = Libro
    fields = ['titulo', 'isbn', 'fecha_publicacion', 'numero_paginas', 'idioma']
    template_name = 'libros/LibroUpdate.html'
    success_url = reverse_lazy('libro:list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, _('Libro creado con exito.'))
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['titulo'].label = _("Titulo")  # Traducción de la etiqueta
        form.fields['isbn'].label = _("ISBN")  # Traducción de la etiqueta
        form.fields['fecha_publicacion'].label = _("Fecha Publicacion")
        form.fields['numero_paginas'].label = _("Numero Paginas")
        form.fields['idioma'].label = _("Idioma")
        return form

@method_decorator([login_required, user_can_delete_update_libro], name='dispatch')
class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'libros/LibroDelete.html'
    success_url = reverse_lazy('libro:list')

    def form_valid(self, form):
        messages.success(self.request, _('Libro borrado con exito.'))
        return super().form_valid(form)


class LibroDetailView(DetailView):
    model = Libro
    template_name = 'libros/LibroDetail.html'
    context_object_name = 'libro'