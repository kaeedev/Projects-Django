from django.contrib import admin

# Register your models here.
from .models import Post

@admin.register(Post) #Registramos el modelo

class PostResource(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'author', 'created_at', 'show_home')

