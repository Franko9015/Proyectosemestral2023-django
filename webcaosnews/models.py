from django.db import models
from django.forms.widgets import ClearableFileInput
from django.contrib.auth.models import User

# Create your models here.

class MultipleImageField(models.ImageField):
    def formfield(self, **kwargs):
        kwargs['widget'] = ClearableFileInput(attrs={'multiple': True})
        return super().formfield(**kwargs)


class Categorias(models.Model):
    nombre=models.CharField(primary_key=True,max_length=45)
    
    def __str__(self) -> str:
        return super().__str__()
    


class Noticia(models.Model):
        idNoticia = models.IntegerField(primary_key=True)
        Titulo = models.CharField(max_length=200)
        Descripcion = models.TextField()
        Ubicacion = models.CharField(max_length=15, default='Desconocido')
        Fotos = MultipleImageField(upload_to='foto', null=True, blank=True)
        miniatura= models.ImageField(upload_to='foto', null=True)
        video = models.FileField(upload_to='video', null=True, blank=True)
        Categorias = models.ForeignKey(Categorias, on_delete=models.CASCADE)
        fecha_publicacion = models.DateTimeField(auto_now_add=True, null=True)
        publicado = models.BooleanField(default=False)
        usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

        def __str__(self):
            return self.Titulo



