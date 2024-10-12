from django.contrib import admin
from django.urls import path, re_path
from django.urls import include
from debug_toolbar.toolbar import debug_toolbar_urls
from .views import Contacto, HomeView, search_view, LoginView, RegistroView, logout_view
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.i18n import set_language

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n'))
] + debug_toolbar_urls()

urlpatterns += i18n_patterns(
    path('set_language/', set_language, name='set_language'),
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name= 'login'),
    path('logout/', logout_view, name= 'logout'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('contact/', Contacto.as_view(), name = 'contacto'),
    path('editorial/', include('books.urls.editorial_url', namespace='editorial')),
    path('autor/', include('books.urls.autor_url', namespace='autor')),
    path('libro/', include('books.urls.libro_url', namespace='libro')),
    path("buscar/", search_view, name="search")
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls'))
    ]