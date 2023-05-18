from django.core.paginator import Paginator
from django.shortcuts import render
from datetime import datetime
from .models import *
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import logout, login as login_aut, authenticate
from django.contrib.auth import views as auth_views
import random


# Create your views here.
import random

def index(request):
    noticias = Noticia.objects.filter(publicado=True)
    paginator = Paginator(noticias, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    noticias_destacadas = []
    if noticias.exists():
        noticias_destacadas = random.sample(list(noticias), min(3, len(noticias)))

    for noticia in noticias:
        noticia.Descripcion = noticia.Descripcion[:140] + "..."
    
    data = {
        'noticia': page_obj,
        'noticia_destacada': noticias_destacadas,
        'numeros_pagina': range(1, paginator.num_pages + 1),
    }
    
    return render(request, "index.html", data)





def economia(request):
    categoria_economia = Categorias.objects.get(nombre='Economia')
    noticias = Noticia.objects.filter(Q(publicado=True) & Q(Categorias=categoria_economia)).order_by('-fecha_publicacion')
    ultimas_noticias = noticias[:6]

    paginator = Paginator(noticias, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'noticias_economia': ultimas_noticias,
        'noticias': page_obj,
    }

    return render(request, "economia.html", data)


def internacional(request):
    categoria_internacional = Categorias.objects.get(nombre='Internacional')
    noticias = Noticia.objects.filter(Q(publicado=True) & Q(Categorias=categoria_internacional))
    
    paginator = Paginator(noticias, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    noticias_destacadas = []
    if noticias.exists():
        noticias_destacadas = random.sample(list(noticias), min(3, len(noticias)))

    for noticia in noticias:
        noticia.Descripcion = noticia.Descripcion[:200] + "..."
    
    data = {'noticias': page_obj, 'noticia_destacada': noticias_destacadas}
    
    return render(request, "Internacional.html", data)



    
def politica(request):
    return render(request, "Politica.html")
def reportaje(request):
    return render(request, "Reportaje.html")
def deportes(request):
    return render(request, "Deportes.html")
def salud(request):
    return render(request, "Salud.html")

def noticia(request,id):
    non= Noticia.objects.get(idNoticia=id)
    data={"item":non}
    return render(request,"noticia.html",data) #Foto Normal

def login(request):
    if request.method == 'POST':
        usern = request.POST.get("ejemplo1")
        cont = request.POST.get("ejemplo2")
        usu = authenticate(request, username=usern, password=cont)
        if usu is not None and usu.is_active:
            login_aut(request, usu)
            return redirect('IND')  # Redireccionar al index después de autenticarse correctamente
        else:
            mensaje = 'Usuario/contraseña inválida'
            return render(request, "ingreso.html", {'mensaje': mensaje})
    else:
        return render(request, "ingreso.html")



def registro(request):
    data={'mensaje':''}
    if request.method == 'POST':
        nom= request.POST.get("Nombre")
        usu= request.POST.get("Usuario")
        ape= request.POST.get("Apellido")
        cor= request.POST.get("Correo")
        cont= request.POST.get("TxtPass1")
        usuario=User()
        usuario.first_name=nom
        usuario.username=usu
        usuario.last_name=ape
        usuario.email=cor
        usuario.set_password(cont)
        try:
            usuario.save()
            data['mensaje']='Grabo Usuario'
        except:
           data['mensaje']='Error al grabar' 
    return render(request, "registro.html",data)


def contacto(request):
    return render(request, "contacto.html")
def indexusuario(request):
    noticias = Noticia.objects.filter(publicado=True)
    paginator = Paginator(noticias, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    noticias_destacadas = []
    if noticias.exists():
        noticias_destacadas = random.sample(list(noticias), min(3, len(noticias)))

    for noticia in noticias:
        noticia.Descripcion = noticia.Descripcion[:140] + "..."
    
    data = {
        'noticia': page_obj,
        'noticia_destacada': noticias_destacadas,
        'numeros_pagina': range(1, paginator.num_pages + 1),
    }
    
    return render(request,"index_usuario.html",data)

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


def buscar_noticias(request):
    # Obtener el término de búsqueda del formulario
    query = request.POST.get('query')

    # Realizar la búsqueda utilizando los filtros de Django
    if query:
        noticias = Noticia.objects.filter(
            Q(usuario__username__icontains=query) |
            Q(usuario__first_name__icontains=query) |
            Q(usuario__last_name__icontains=query) |
            Q(Titulo__icontains=query) |
            Q(Categorias__nombre__icontains=query)
        )
    else:
        noticias = Noticia.objects.all()

    # Renderizar la plantilla con las noticias encontradas y los parámetros de búsqueda
    return render(request, 'resultado_busqueda.html', {'noticias': noticias, 'query': query})




def adminnoticia(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        for key, value in request.POST.items():
            if key.startswith('opcion_'):
                # Obtener el ID de la noticia
                noticia_id = key.replace('opcion_', '')
                # Obtener el estado seleccionado (aprobado o rechazado)
                estado = value
                # Aprobar o eliminar la noticia según el estado
                if estado == 'aprobado':
                    noticia = get_object_or_404(Noticia, idNoticia=noticia_id)
                    noticia.publicado = True
                    noticia.save()
                elif estado == 'rechazado':
                    Noticia.objects.filter(idNoticia=noticia_id).delete()

        # Redirigir nuevamente a la página de administración de noticias
        return redirect('ADMNON')

    # Obtener todas las noticias no publicadas
    noticias = Noticia.objects.filter(publicado=False)
    context = {'noticias': noticias}
    return render(request, 'administrador.html', context)

def logout(request):
    return auth_views.LogoutView.as_view(next_page='IND')(request)
