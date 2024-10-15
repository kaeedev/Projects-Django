
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.i18n import set_language, i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('ckeditor/', include('ckeditor_uploader.urls'))
] + debug_toolbar_urls() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += i18n_patterns(
    path('set_language/', set_language, name='set_language'),
    path('', include('core.urls', namespace='core')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('courses/', include('courses.urls', namespace='courses')),
    path('admin/', admin.site.urls),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls'))
    ]