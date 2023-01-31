from django.shortcuts import render, get_object_or_404
from servicios.models import Servicios


def servicios(request):
    
    servicios = Servicios.objects.all()
    datos = {
        "servicios":servicios
    }
    return render(request, 'servicios.html', datos)

# Create your views here.
