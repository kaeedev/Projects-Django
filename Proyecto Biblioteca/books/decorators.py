from books.models import Editorial, Libro, Autor
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

def user_can_delete_update_editorial(function):
    def wrap(request, *args, **kwargs):
        try:
            editorial = Editorial.objects.get(pk=kwargs['pk'])
        except Editorial.DoesNotExist:
            raise Http404
        
        if request.user == editorial.created_by:
            return function(request, *args, **kwargs)
        return render(request, 'errors/permission_denied_editorial.html', status=403)
    
    return wrap

def user_can_delete_update_autor(function):
    def wrap(request, *args, **kwargs):
        try:
            autor = Autor.objects.get(pk=kwargs['pk'])
        except Autor.DoesNotExist:
            raise Http404
        
        if request.user == autor.created_by:
            return function(request, *args, **kwargs)
        return render(request, 'errors/permission_denied_autor.html', status=403)
    
    return wrap

def user_can_delete_update_libro(function):
    def wrap(request, *args, **kwargs):
        try:
            libro = Libro.objects.get(pk=kwargs['pk'])
        except Libro.DoesNotExist:
            raise Http404
        
        if request.user == libro.created_by:
            return function(request, *args, **kwargs)
        return render(request, 'errors/permission_denied_libro.html', status=403)
    
    return wrap