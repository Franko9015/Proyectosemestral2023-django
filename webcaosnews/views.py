from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")
def economia(request):
    return render(request,"Economia.html")
def internacional(request):
    return render(request, "Internacional.html")
def politica(request):
    return render(request, "Politica.html")
def reportaje(request):
    return render(request, "Reportaje.html")
def deportes(request):
    return render(request, "Deportes.html")
def salud(request):
    return render(request, "Salud.html")
def noticia1(request):
    return render(request, "plantilla_noticias_carrusel.html")
def noticia2(request):
    return render(request, "plantilla_noticias_video.html")
def noticia3(request):
    return render(request, "plantilla_noticias_fotos.html")
def login(request):
    return render(request, "ingreso.html")
def registro(request):
    return render(request, "registro.html")
def contacto(request):
    return render(request, "contacto.html")