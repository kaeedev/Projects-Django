from django.urls import path

from .views import home_view, about_us, register, login_view, avisoslegales, logout_view, ContactoForm
app_name='core'

urlpatterns = [
    #path('contact-with-us/', contact_view, name= 'contacto'),
    path('contact-with-us/ccbv/', ContactoForm.as_view(), name= 'contacto_ccbv'),
    path('', home_view, name= 'home'),
    path('about_us/', about_us, name= 'about_us'),
    path('register/', register, name= 'register'),
    path('login/', login_view, name= 'login'),
    path('logout/', logout_view, name= 'logout'),
    path('avisoslegales/', avisoslegales, name= 'avisoslegales'),
    #path('prueba/', Prueba.as_view(), name= 'prueba'),
    #path('pruebatemplateview/', PruebaTemplateView.as_view(), name= 'pruebatemplateview')
]