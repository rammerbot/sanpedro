from albums.models import Fotos, Albums

def albums(request):

    albums = Albums.objects.all()
    fotos = Fotos.objects.all()

    return {
        "albums":albums,
        "fotos": fotos
    }