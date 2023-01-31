from django.urls import path
from . import views

urlpatterns = [

    path("albums/", views.albums, name="Albums"),
    path("fotos/<int:categorias_id>",views.fotos, name="Fotos"),
    path("todos/",views.todos, name="Todos"),
    path("mascota/<int:mascota_id>",views.mascota, name="Mascota")
   
]