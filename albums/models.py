from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Albums(models.Model):

    categoria = models.CharField(max_length=50, verbose_name="Categoria")
    descripcion = RichTextField(verbose_name="Descripcion")
    imagen = models.ImageField(verbose_name="Imagen", upload_to='media')
    fecha_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"

    def __str__(self):
        return self.categoria

class Fotos(models.Model):
    mascota = models.CharField(max_length=50, verbose_name="Mascota")
    foto = models.ImageField(verbose_name="Foto", upload_to='media')
    descripcion = models.CharField(max_length=20, verbose_name="Descripcion")
    categoria = models.ForeignKey(Albums, on_delete=models.CASCADE)
    fecha_at= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"

    def __str__(self):
        return self.mascota
    

