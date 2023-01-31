from django.db import models
from ckeditor.fields import RichTextField


class Categoria(models.Model):

    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    descripcion = RichTextField(verbose_name="Descripcion")
    imagen = models.ImageField(default="null",verbose_name="Imagen", upload_to='media')
    visible = models.BooleanField(verbose_name="Visible")
    orden = models.IntegerField(default=0, verbose_name="Orden")


    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    def __str__(self):
        return self.nombre

class Servicios(models.Model):

    servicio = models.CharField(max_length=50, verbose_name="Servicio")
    descripcion = RichTextField(verbose_name="Descripcion")
    imagen = models.ImageField(verbose_name="Imagen", upload_to='media')
    categoria = models.ManyToManyField(Categoria, verbose_name="Categorias",blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
    
    def __str__(self):
        return self.servicio



# Create your models here.
