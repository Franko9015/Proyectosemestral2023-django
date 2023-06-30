from django.contrib import admin
from django.urls import path
from .views import * 
 


#Ejemplo
#path('',index,name='IND'),
#path('galeria/',galeria,name='GALE'),
#path('quienes/',quienes,name='QUIEN'),
#path('formulario/',formulario,name='FORMU'),


urlpatterns = [
    path('',index,name='IND'),
    path('perfil/<str:username>/', perfil, name='PEF'),
    path('editar/<str:username>/', editar_perfil, name='EDP'),
    path('economia/',economia,name='ECO'),
    path('internacional/',internacional,name='INT'),
    path('politica/',politica,name='POL'),
    path('reportajes/',reportaje,name='REP'),
    path('salud/',salud,name='SAL'),
    path('deportes/',deportes,name='DEP'),
    path('Login/',login,name='LOG'),
    path('Registro/',registro,name='REG'),
    path('Contacto/',contacto,name='CON'),
    path('Noticia/<id>/', noticia, name='NON'),
    path('AgregarNoticia/',ingresarnoticia,name='AGRNON'),
    path('AdministradorNoticia/',adminnoticia,name='ADMNON'),
    path('buscar/',buscar_noticias,name='BUSCAR'),
    path('Editot/<id>/',editar_noticia,name='EDN'),
    path('EstadoN/',estado_noticia,name='EST'),
    path('logout/', auth_views.LogoutView.as_view(next_page='IND'), name='LOGOUT'),
]