# Generated by Django 4.1.3 on 2022-12-23 17:37

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=50, verbose_name='Categoria')),
                ('descripcion', ckeditor.fields.RichTextField(verbose_name='Descripcion')),
                ('imagen', models.ImageField(upload_to='media', verbose_name='Imagen')),
                ('fecha_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
            },
        ),
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mascota', models.CharField(max_length=50, verbose_name='Mascota')),
                ('foto', models.ImageField(upload_to='media', verbose_name='Foto')),
                ('descripcion', models.CharField(max_length=10, verbose_name='Descripcion')),
                ('fecha_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.albums')),
            ],
            options={
                'verbose_name': 'Foto',
                'verbose_name_plural': 'Fotos',
            },
        ),
    ]
