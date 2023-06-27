from django.db import models
from django.forms.widgets import ClearableFileInput
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission

# Create your models here.



class Categorias(models.Model):
    nombre=models.CharField(primary_key=True,max_length=45)
    
    def __str__(self) -> str:
        return super().__str__()
    
class Noticia(models.Model):
    idNoticia = models.IntegerField(primary_key=True)
    Titulo = models.CharField(max_length=200)
    Descripcion = models.TextField()
    Ubicacion = models.CharField(max_length=15, default='Desconocido')
    Fotos = models.ImageField(upload_to='foto', null=True, blank=True)
    miniatura = models.ImageField(upload_to='foto', null=True)
    video = models.FileField(upload_to='video', null=True, blank=True)
    Categorias = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True, null=True)
    publicado = models.BooleanField(default=False)
    comentario = models.CharField(max_length=200, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
    ]
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return self.Titulo

class Comentarios(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='comentarios')
    comentario_padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='respuestas')
    
    def __str__(self):
        return f"Comentario por {self.usuario.username}"