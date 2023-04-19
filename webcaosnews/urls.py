
from django.contrib import admin
from django.urls import path
from .views import index

#Ejemplo
#path('',index,name='IND'),
#path('galeria/',galeria,name='GALE'),
#path('quienes/',quienes,name='QUIEN'),
#path('formulario/',formulario,name='FORMU'),


urlpatterns = [
    path('',index,name='IND'),
]