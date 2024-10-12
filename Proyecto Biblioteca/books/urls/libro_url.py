
from django.urls import path
from books.views import (
    LibroListView,
    LibroCreateView,
    LibroUpdateView,
    LibroDeleteView,
    LibroDetailView

)
app_name = 'libro'

urlpatterns = [
    path('lista/', LibroListView.as_view(), name='list'),
    path('create/', LibroCreateView.as_view(), name='create'),
    path('update/<pk>', LibroUpdateView.as_view(), name='update'),
    path('delete/<pk>', LibroDeleteView.as_view(), name='delete'),
    path('detail/<pk>', LibroDetailView.as_view(), name='detail')
    
] 
