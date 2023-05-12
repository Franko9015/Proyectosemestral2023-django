from django.core.paginator import Paginator
from django.shortcuts import render
from datetime import datetime
from .models import *
import random
from django.http import JsonResponse
from django.views.decorators.http import require_POST      

# Create your views here.
def index(request):
    noticias = Noticia.objects.all()
    paginator = Paginator(noticias, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    noticias_destacadas = random.sample(list(noticias), 3)
    for noticia in noticias:
        noticia.Descripcion = noticia.Descripcion[:140] + "..."
    data = {
        'noticia': page_obj,
        'noticia_destacada': noticias_destacadas,
        'numeros_pagina': range(1, paginator.num_pages + 1),
    }
    return render(request, "index.html", data)




def economia(request):
    return render(request,"Economia.html")

def internacional(request):
    categoria_internacional = Categorias.objects.get(nombre='Internacional')
    internacional = Noticia.objects.filter(Categorias=categoria_internacional)
    for noticia in internacional:
        noticia.Descripcion = noticia.Descripcion[:200] + "..."
    data = {'noticias': internacional}
    return render(request, "Internacional.html", data)



    
def politica(request):
    return render(request, "Politica.html")
def reportaje(request):
    return render(request, "Reportaje.html")
def deportes(request):
    return render(request, "Deportes.html")
def salud(request):
    return render(request, "Salud.html")
def noticia1(request):
    return render(request, "plantilla_noticias_fotos_carrusel.html") #Foto Carrusel
def noticia2(request):
    return render(request, "plantilla_noticias_video.html")

def noticia3(request,id):
    non= Noticia.objects.get(idNoticia=id)
    data={"item":non}
    return render(request,"plantilla_noticias_fotos.html",data) #Foto Normal

def login(request):
    return render(request, "ingreso.html")
def registro(request):
    return render(request, "registro.html")
def contacto(request):
    return render(request, "contacto.html")
def indexusuario(request):
    return render(request,"index_usuario.html")

def ingresarnoticia(request):
    cate = Categorias.objects.all()
    data = {'categorias': cate}

def ingresarnoticia(request):
    cate = Categorias.objects.all()
    data = {'categorias': cate}

    if request.method == 'POST':
        id = request.POST.get("txtid")
        nom = request.POST.get("txtnombre")
        desc = request.POST.get("txtdesc")
        ubi = request.POST.get("txtubicacion")
        cate = request.POST.get("cbocategoria")
        miniatura = request.FILES.get("txtminiatura")
        fotos = request.FILES.get("txtfotos")
        videos = request.FILES.get("txtvideos")
        categoria = Categorias.objects.get(nombre=cate)

        # Creamos la noticia y guardamos las imágenes y los videos subidos
        noticia = Noticia(
            idNoticia=id,
            Titulo=nom,
            Descripcion=desc,
            Ubicacion=ubi,
            Categorias=categoria,
            miniatura=miniatura,
            Fotos=fotos,
            video=videos,
            usuario=request.user, # agregar usuario
            fecha_publicacion=datetime.now()  # Usamos la fecha y hora actuales  
        )

        noticia.save() # guardar la noticia en la base de datos
        data['mensaje'] = "Noticia guardada con éxito."

    return render(request, "agregar_noticias.html", data)







def adminnoticia(request):
    noticias = Noticia.objects.filter(publicado=False)
    context = {'noticias': noticias}
    return render(request, 'administrador.html', context)


