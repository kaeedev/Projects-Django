from django import forms 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.Form):
    nombre = forms.CharField(
        label=_('Nombre'),
        max_length=100
    )
    email = forms.EmailField(label=_('Email'))
    comentario = forms.CharField(label=_('Comentario'), max_length=1000, widget=forms.Textarea)
    #lo ultimo es para que aparezca como un textarea

    def clean_comentario(self):
        comentario = self.cleaned_data.get('comentario')
        if len(comentario) < 5:
            raise forms.ValidationError('El comentario debe tener al menos 5 caracteres')
        return comentario
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres')
        return nombre


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=140, label=_('Nombre de usuario'))
    password = forms.CharField(label= _('Contraseña'), widget= forms.PasswordInput())

class SearchForm(forms.Form):
    busqueda = forms.CharField(label=_('Buscar'), max_length=300)

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label=_("Correo electrónico"))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': _("Nombre de usuario"),
            'email': _("Email"),
            'password1': _("Contraseña"),
            'password2': _("Confirmar contraseña"),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Las contraseñas no coinciden."))

        return cleaned_data