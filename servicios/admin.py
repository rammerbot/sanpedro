from django.contrib import admin
from .models import Servicios, Categoria


admin.site.register(Servicios)
admin.site.register(Categoria)

# Register your models here.


header = "Gestor de sitio Web \"San Pedro\""
title = "San Pedro"
subtitulo = "Panel de Administracion"

admin.site.site_header = header
admin.site.site_title = title
admin.site.index_title = subtitulo