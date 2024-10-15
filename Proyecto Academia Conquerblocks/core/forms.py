from django import forms
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=50, label=_("Nombre"))
    email = forms.EmailField(label="Email")
    comentario = forms.CharField(max_length=1000, label=_("Comentario"), widget=forms.Textarea)

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 5:
            raise forms.ValidationError(_("El nombre debe tener al menos 5 caracteres"))
        return nombre


class LoginForm(forms.Form):
    username = forms.CharField(max_length=140, label=_("Nombre de usuario"))
    password = forms.CharField(widget=forms.PasswordInput(), label=_("Contraseña"))


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=140, label=_("Nombre de usuario"))
    first_name = forms.CharField(max_length=140, label=_("Nombre"))
    last_name = forms.CharField(max_length=140, label=_("Apellidos"))
    email = forms.EmailField(max_length=140, label=_("Email"))

    password1 = forms.CharField(label=_('Contraseña'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Repita su contraseña'), widget=forms.PasswordInput)


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2 and password1 != '':
            raise forms.ValidationError(_('Las contraseñas no coinciden'))

        if password2 != '':
            validate_password(password2)

        return password2