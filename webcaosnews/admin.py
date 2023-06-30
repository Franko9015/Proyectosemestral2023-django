from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Categorias)
admin.site.register(Noticia)
admin.site.register(Comentarios)
admin.site.register(PerfilUsuario)