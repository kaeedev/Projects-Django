from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact) #Registramos el modelo

class ContactResource(admin.ModelAdmin):
    model = Contact
    list_display = ('nombre','email', 'contactado', 'created_at')
    list_filter = ('contactado',)
