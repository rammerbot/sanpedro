from django.shortcuts import render


def layout(request):


    contenido = "<p>dsfsdfadsfdsfadslfkjasdk<p>"
    
    return render(request, "index/index.html",{
        "titulo":"Inicio",
        "contenido":contenido
    })

# Create your views here.

