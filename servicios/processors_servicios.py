from servicios.models import Categoria, Servicios

def categoria(request):
    
    servicios = Servicios.objects.values_list("categoria","servicio")
    categorias = Categoria.objects.all()

    return {

        "servi_menu":servicios,
        "categorias":categorias
    }
