from django.shortcuts import render, get_object_or_404
from .models import Fotos, Albums
from django.db.models import Q

# Create your views here.

def albums(request):
  busqueda = request.GET.get("buscar")
  categories = Albums.objects.all()
  pictures = Fotos.objects.all()

  if busqueda:
    pictures = Fotos.objects.filter(
      Q(mascota__icontains=busqueda)
    )

  return render(request, "albums/albums.html",{
      "titulo":"Albums",
      "fotografias":pictures,
      "albumes":categories,
    })

def fotos(request, categorias_id):

  
  pic = Fotos.objects.filter(categoria=categorias_id).all()
  

  return render(request, "albums/fotos.html",{
    "titulo":"Album",
    "pic":pic,
  })

def todos(request):

  busqueda = request.GET.get("buscar")
  fotos = Fotos.objects.all()

  if busqueda:
    fotos = Fotos.objects.filter(
      Q(mascota__icontains=busqueda)
    )



  return render(request, "albums/todos.html",{
    "titulo":"General",
    "pictures":fotos
  })

def mascota(request, mascota_id):

  fotos = Fotos.objects.filter(id=mascota_id).all()

  return render(request, "albums/mascota.html",{
    "titulo":"Mascotas",
    "pictures":fotos
  })