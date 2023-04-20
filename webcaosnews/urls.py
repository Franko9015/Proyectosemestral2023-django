
from django.contrib import admin
from django.urls import path
from .views import index
from .views import economia
from .views import internacional 
from .views import politica
from .views import reportaje
from .views import deportes
from .views import salud
from .views import noticia1
from .views import noticia2
from .views import noticia3
from .views import login
from .views import registro
from .views import contacto

#Ejemplo
#path('',index,name='IND'),
#path('galeria/',galeria,name='GALE'),
#path('quienes/',quienes,name='QUIEN'),
#path('formulario/',formulario,name='FORMU'),


urlpatterns = [
    path('',index,name='IND'),
    path('economia/',economia,name='ECO'),
    path('internacional/',internacional,name='INT'),
    path('politica/',politica,name='POL'),
    path('reportajes/',reportaje,name='REP'),
    path('salud/',salud,name='SAL'),
    path('deportes/',deportes,name='DEP'),
    path('Login/',login,name='LOG'),
    path('Registro/',registro,name='REG'),
    path('Contacto/',contacto,name='CON'),
    path('NoticiaEjemplo1/',noticia1,name='NON1'),
    path('NoticiaEjemplo2/',noticia2,name='NON2'),
    path('NoticiaEjemplo3/',noticia3,name='NON3'),
]