from django.shortcuts import render, redirect # type: ignore
from books.models import Autor, Libro, Editorial
from books.forms import SearchForm
from .form import ContactForm
from .models import Contact
from django.views.generic.edit import FormView # type: ignore
from .form import ContactForm, LoginForm, RegistroForm
from django.core.mail import send_mail # type: ignore
from django.views.generic.base import TemplateView # type: ignore
from django.urls import reverse_lazy # type: ignore
from django.views.generic import ListView
from django.contrib.auth import login, logout
from django.urls import reverse
from django.contrib import messages
from django.utils.translation import gettext as _
from django.http import HttpResponseRedirect
from django.utils import translation
from django.views.generic import View
from django.views.generic import CreateView
#Vistas generales de la aplicacion


class HomeView(TemplateView):
    template_name = 'general/home.html'

    def get(self, request, *args, **kwargs):
        # Añadir un mensaje de éxito
        messages.info(request, _('¡Bienvenido a la página! En esta página podrás consultar nuestros Libros, Editoriales y Autores.'))


        return super().get(request, *args, **kwargs)


def search_view(request):
    if request.GET:
        formulario = SearchForm(request.GET)

        busqueda = formulario.data['q']

        autores = Autor.objects.filter(nombre__icontains=busqueda)
        editoriales = Editorial.objects.filter(nombre__icontains=busqueda)
        libros = Libro.objects.filter(titulo__icontains=busqueda)

        context = {
            'autores': autores,
            'editoriales': editoriales,
            'libros': libros,
            'formulario': formulario
        }

        return render(request, "general/search.html", context)
    else:
        formulario = SearchForm()

    context = {
        'formulario' : formulario
    }

    return render(request, "general/search.html", context)


class Contacto(FormView):
    template_name = 'general/contacto.html'
    form_class = ContactForm
    success_url = reverse_lazy('contacto')

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        email = form.cleaned_data['email']
        comentario = form.cleaned_data['comentario']
        message_content = f'{nombre} con email {email} ha escrito lo siguiente: {comentario}'

        Contact.objects.create(
        nombre=nombre,
        email=email,
        comentario=comentario
        )

        success = send_mail(
            'Formulario de contacto de mi Web',
            message_content,
            'lalbertohab@gmail.com',
            ['l.alberto3.albvisop@hotmail.com'],
            fail_silently=False
        )

        messages.success (self.request, _('El correo se ha enviado correctamente. Contactaremos contigo en breves'))
        return super().form_valid(form)
    

class LoginView(FormView):
    template_name = 'general/login.html'
    form_class = LoginForm
    def get(self, request, *args, **kwargs):
        # Añadir un mensaje de éxito
        messages.info(request, _('Es necesario logearse para realizar algunas acciones como crear nuevos elementos, editarlos o borrarlos.'))

        return super().get(request, *args, **kwargs)
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        messages.success(self.request, _('Te has logeado satisfactoriamente'))
        return redirect('home')
    
    def form_invalid(self, form):
        messages.error(self.request, _('Usuario o contraseña no validos.'))
        return super().form_invalid(form)


class RegistroView(CreateView):
    form_class = RegistroForm
    template_name = 'general/registro.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, _("Registro exitoso."))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _("Hubo un error en el registro."))
        return super().form_invalid(form)
    
    def get(self, request, *args, **kwargs):
        # Añadir un mensaje de éxito
        messages.info(request, _('Se recomienda crear una cuenta para poder editar, borrar o crear nuevos datos.'))

        return super().get(request, *args, **kwargs)
    
    
def logout_view(request):
    logout(request)
    messages.success(request, _('Has cerrado sesion satisfactoriamente'))
    return redirect(reverse('home'))

