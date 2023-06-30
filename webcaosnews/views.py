from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.models import Group
from datetime import datetime
from .models import *
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import logout, login as login_aut, authenticate
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import views as auth_views
import random
from django.urls import reverse



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
        'numeros_pagina': range(1, paginator.num_pages + 1),
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
    
    data = {'noticias': page_obj, 'noticia_destacada': noticias_destacadas, 'numeros_pagina': range(1, paginator.num_pages + 1),}
    
    return render(request, "Internacional.html", data)



    
def politica(request):
    categoria_politica = Categorias.objects.get(nombre='Politica')
    noticias = Noticia.objects.filter(Q(publicado=True) & Q(Categorias=categoria_politica)).order_by('-fecha_publicacion')
    ultimas_noticias = noticias[:6]

    paginator = Paginator(noticias, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'noticias_politica': ultimas_noticias,
        'noticias': page_obj,
        'numeros_pagina': range(1, paginator.num_pages + 1),
    }

    return render(request, "Politica.html", data)


def reportaje(request):
    categoria_reportajes = Categorias.objects.get(nombre='Reportaje')
    noticias = Noticia.objects.filter(Q(publicado=True) & Q(Categorias=categoria_reportajes))
    
    paginator = Paginator(noticias, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    noticias_destacadas = []
    if noticias.exists():
        noticias_destacadas = random.sample(list(noticias), min(3, len(noticias)))

    for noticia in noticias:
        noticia.Descripcion = noticia.Descripcion[:200] + "..."
    
    data = {'noticias': page_obj, 'noticia_destacada': noticias_destacadas, 'numeros_pagina': range(1, paginator.num_pages + 1),}
    
    return render(request, "Reportaje.html",data)


def deportes(request):
    categoria_deportes = Categorias.objects.get(nombre='Deporte')
    noticias = Noticia.objects.filter(Q(publicado=True) & Q(Categorias=categoria_deportes)).order_by('-fecha_publicacion')
    ultimas_noticias = noticias[:6]

    paginator = Paginator(noticias, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'noticias_deportes': ultimas_noticias,
        'noticias': page_obj,
        'numeros_pagina': range(1, paginator.num_pages + 1),
    }
    return render(request, "Deportes.html",data)

def salud(request):
    categoria_salud = Categorias.objects.get(nombre='Salud')
    noticias = Noticia.objects.filter(Q(publicado=True) & Q(Categorias=categoria_salud))
    
    paginator = Paginator(noticias, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    data = {'noticias': page_obj,
    'noticias_salud': noticias,
    'numeros_pagina': range(1, paginator.num_pages + 1) }
    return render(request, "Salud.html",data)


def noticia(request, id):
    # Obtener la noticia correspondiente al ID proporcionado
    noticia = get_object_or_404(Noticia, idNoticia=id)

    # Obtener los comentarios asociados a la noticia y sus respuestas
    comentarios = Comentarios.objects.filter(noticia=noticia, comentario_padre=None).prefetch_related('respuestas')

    # Obtener los artículos más leídos
    articulos_mas_leidos = Noticia.objects.filter(publicado=True).exclude(idNoticia=id).order_by('-fecha_publicacion')[:5]

    # Verificar si el usuario está autenticado
    if request.user.is_authenticated:
        # Procesar el formulario de comentario enviado
        if request.method == 'POST':
            comentario_texto = request.POST.get('comment-text', '')
            comentario_padre_id = request.POST.get('comentario-padre-id', None)

            if comentario_padre_id:
                comentario_padre = Comentarios.objects.get(id=comentario_padre_id)
                nuevo_comentario = Comentarios(usuario=request.user, texto=comentario_texto, noticia=noticia, comentario_padre=comentario_padre)
            else:
                nuevo_comentario = Comentarios(usuario=request.user, texto=comentario_texto, noticia=noticia)

            nuevo_comentario.save()
            # Redireccionar a la misma página después de agregar el comentario
            return redirect('NON', id=id)

    # Crear un diccionario con los datos a pasar a la plantilla
    data = {
        'noticia': noticia,  # La noticia actual
        'comentarios': comentarios,  # Los comentarios asociados a la noticia
        'articulos_mas_leidos': articulos_mas_leidos,  # Los artículos más leídos
    }

    # Renderizar la plantilla "noticia.html" con los datos
    return render(request, "noticia.html", data)




def login(request):
    if request.method == 'POST':
        usern = request.POST.get("ejemplo1")
        cont = request.POST.get("ejemplo2")
        usu = authenticate(request, username=usern, password=cont)
        
        if usu is not None and usu.is_active:
            grupos = usu.groups.all()
            if grupos.exists():
                request.session['role'] = grupos[0].name
            else:
                request.session['role'] = 'lector'  # Establecer 'lector' como el grupo por defecto si el usuario no tiene grupos asignados
            login_aut(request, usu)
            return redirect('IND')
        else:
            mensaje = 'Usuario/contraseña inválida'
            return render(request, "ingreso.html", {'mensaje': mensaje})
    else:
        return render(request, "ingreso.html")



def registro(request):
    data = {'mensaje': ''}
    if request.method == 'POST':
        nom = request.POST.get("Nombre")
        usu = request.POST.get("Usuario")
        ape = request.POST.get("Apellido")
        cor = request.POST.get("Correo")
        cont = request.POST.get("TxtPass1")
        fecha_nac = request.POST.get("FechaNacimiento")
        usuario = User()
        usuario.first_name = nom
        usuario.username = usu
        usuario.last_name = ape
        usuario.email = cor
        usuario.set_password(cont)
        try:
            usuario.save()
            perfil = PerfilUsuario()
            perfil.user = usuario
            perfil.fecha_nacimiento = datetime.strptime(fecha_nac, '%Y-%m-%d').date()
            perfil.save()
            grupo_lector = Group.objects.get(name='lector')
            usuario.groups.add(grupo_lector)
            data['mensaje'] = 'Usuario registrado exitosamente'
        except:
            data['mensaje'] = 'Error al registrar el usuario'
    return render(request, "registro.html", data)


def contacto(request):
    return render(request, "contacto.html")
    
    data = {
        'noticia': page_obj,
        'noticia_destacada': noticias_destacadas,
        'numeros_pagina': range(1, paginator.num_pages + 1),
    }
    
    return render(request,"index_usuario.html",data)


@login_required(login_url='/Login/')
@permission_required('webcaosnews.add_noticia')
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


@login_required(login_url='/Login/')
@permission_required('webcaosnews.change_noticia')
def adminnoticia(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('opcion_'):
                noticia_id = key.replace('opcion_', '')
                estado = value
                observaciones = request.POST.get('observaciones_' + noticia_id, '')
                noticia = get_object_or_404(Noticia, idNoticia=noticia_id)
                if estado == 'aprobado':
                    noticia.publicado = True
                    noticia.comentario = ''
                    noticia.estado = 'aprobado'  # Cambiar el estado a "aprobado"
                elif estado == 'rechazado':
                    noticia.publicado = False
                    noticia.comentario = observaciones
                    noticia.estado = 'rechazado'  # Cambiar el estado a "rechazado"
                noticia.save()

        return redirect('ADMNON')

    noticias = Noticia.objects.filter(estado='pendiente', comentario='')
    context = {'noticias': noticias}
    return render(request, 'administrador.html', context)



@login_required(login_url='/Login/')
@permission_required(['webcaosnews.change_noticia', 'webcaosnews.delete_noticia'])
def estado_noticia(request):
    if request.method == 'POST':
        # Obtener los datos del formulario y procesarlos
        for key, value in request.POST.items():
            if key.startswith('observaciones_'):
                # Obtener el ID de la noticia
                noticia_id = key.replace('observaciones_', '')
                # Obtener las observaciones o motivos
                observaciones = value
                # Actualizar el comentario y el estado de la noticia
                noticia = get_object_or_404(Noticia, idNoticia=noticia_id)
                noticia.comentario = observaciones
                if observaciones:
                    noticia.estado = 'rechazado'
                else:
                    noticia.estado = 'pendiente'
                noticia.save()

            elif key.startswith('eliminar_'):
                # Obtener el ID de la noticia a eliminar
                noticia_id = key.replace('eliminar_', '')
                # Eliminar la noticia
                noticia = get_object_or_404(Noticia, idNoticia=noticia_id)
                noticia.delete()

        # Redirigir nuevamente a la página de estado de noticia
        return redirect('EST')

    # Verificar el grupo de usuario del solicitante
    role = request.session.get('role')

    if role == 'supervisor' or request.user.is_superuser:
        # Si es Supervisor o Superadmin, obtener todas las noticias
        noticias = Noticia.objects.all()
    elif role == 'periodista':
        # Si es Periodista, obtener solo sus propias noticias
        noticias = Noticia.objects.filter(usuario=request.user)
    else:
        # Si no tiene un grupo específico, no mostrar ninguna noticia
        noticias = []

    context = {'noticias': noticias}
    return render(request, 'estado.html', context)



def perfil(request, username):
    user = get_object_or_404(User, username=username)
    perfil_usuario = get_object_or_404(PerfilUsuario, user=user)

    noticias_periodista = []
    ultimos_comentarios = []

    if user.groups.filter(name='periodista').exists() or user.is_superuser:
        noticias_periodista = Noticia.objects.filter(usuario=user)

    if user.groups.filter(name='lector').exists() or user.is_superuser:
        ultimos_comentarios = Comentarios.objects.filter(usuario=user).order_by('-fecha')[:5]
    
    is_owner = request.user == user  # Verificar si el usuario autenticado es el propietario del perfil

    data = {
        'user': user,
        'perfil_usuario': perfil_usuario,
        'noticias_periodista': noticias_periodista,
        'ultimos_comentarios': ultimos_comentarios,
        'is_owner': is_owner  # Pasar el indicador de propiedad al contexto
    }

    return render(request, 'perfil.html', data)

@login_required(login_url='/Login/')
def editar_perfil(request, username):
    user = User.objects.get(username=username)
    perfil_usuario, created = PerfilUsuario.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        fotoperfil = request.FILES.get("id_foto_perfil")
        descripcion = request.POST.get("iddescripcion")
        twitter = request.POST.get("idtwitter")
        instagram = request.POST.get("idinstagram")
        facebook = request.POST.get("idfacebook")

        perfil_usuario.foto_perfil = fotoperfil
        perfil_usuario.descripcion = descripcion
        perfil_usuario.twitter = twitter
        perfil_usuario.instagram = instagram
        perfil_usuario.facebook = facebook

        perfil_usuario.save()
        mensaje = "Perfil actualizado con éxito."
        data = {
            'username': username,
            'mensaje': mensaje,
        }
        return redirect(reverse('PEF', kwargs={'username': username}))
    
    data = {
        'username': username,
    }
    return render(request, 'editarperfil.html', data)




@login_required(login_url='/Login/')
@permission_required('webcaosnews.change_noticia')
def editar_noticia(request, id):
    cate = Categorias.objects.all()
    noticia = get_object_or_404(Noticia, idNoticia=id)
    data = {'categorias': cate, 'noticia': noticia}

    if request.method == 'POST':
        nom = request.POST.get("txtnombre")
        desc = request.POST.get("txtdesc")
        ubi = request.POST.get("txtubicacion")
        cate = request.POST.get("cbocategoria")
        miniatura = request.FILES.get("txtminiatura")
        fotos = request.FILES.get("txtfotos")
        videos = request.FILES.get("txtvideos")
        categoria = Categorias.objects.get(nombre=cate)

        # Actualizamos los campos de la noticia existente
        noticia.Titulo = nom
        noticia.Descripcion = desc
        noticia.Ubicacion = ubi
        noticia.Categorias = categoria
        noticia.miniatura = miniatura
        noticia.Fotos = fotos
        noticia.video = videos
        noticia.estado = 'pendiente'  # Cambiamos el estado a "pendiente"
        noticia.comentario = ''  # Eliminamos el comentario de rechazo

        noticia.save()  # guardar la noticia actualizada en la base de datos
        data['mensaje'] = "Noticia actualizada con éxito."

        return redirect('EST') # Redirigir a la página de estado de noticia
    return render(request, "Editar_noticia.html", data)



def logout(request):
    return auth_views.LogoutView.as_view(next_page='IND')(request)
