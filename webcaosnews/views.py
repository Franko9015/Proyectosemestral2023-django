from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *
import random

# Create your views here.
def index(request):
    noticias = Noticia.objects.all()
    paginator = Paginator(noticias, 6)
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

    if request.method == 'POST':
        id = request.POST.get("txtid")
        nom = request.POST.get("txtnombre")
        desc = request.POST.get("txtdesc")
        ubi = request.POST.get("txtubicacion")
        cate = request.POST.get("cbocategoria")
        categoria = Categorias.objects.get(nombre=cate)

        # Obtenemos los archivos subidos por el usuario
        archivos = request.FILES.getlist('archivo')

        # Creamos una lista para almacenar las imágenes y los videos subidos
        imagenes = []
        videos = []

        # Separamos las imágenes y los videos en listas diferentes
        for archivo in archivos:
            if archivo.content_type.split('/')[0] == 'foto':
                imagenes.append(archivo)
            elif archivo.content_type.split('/')[0] == 'video':
                videos.append(archivo)

        # Creamos la noticia y guardamos las imágenes y los videos subidos
        noticia = Noticia(
            idNoticia=id,
            Titulo=nom,
            Descripcion=desc,
            Ubicacion=ubi,
            Categorias=categoria,
        )

        # Guardamos las imágenes
        for imagen in imagenes:
            noticia.foto = imagen
            noticia.save()

        # Guardamos los videos
        for video in videos:
            Video.objects.create(noticia=noticia, archivo=video)

        data['mensaje'] = "Noticia guardada con éxito."

    return render(request, "agregar_noticias.html", data)



def adminnoticia(request):
    noticias = Noticia.objects.filter(publicado=False)
    context = {'noticias': noticias}
    return render(request, 'administrador.html', context)

