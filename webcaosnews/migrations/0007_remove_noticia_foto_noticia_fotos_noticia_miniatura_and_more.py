# Generated by Django 4.2 on 2023-05-18 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcaosnews', '0006_noticia_ubicacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='foto',
        ),
        migrations.AddField(
            model_name='noticia',
            name='Fotos',
            field=models.ImageField(blank=True, null=True, upload_to='foto'),
        ),
        migrations.AddField(
            model_name='noticia',
            name='miniatura',
            field=models.ImageField(null=True, upload_to='foto'),
        ),
        migrations.AddField(
            model_name='noticia',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='video'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='Titulo',
            field=models.CharField(max_length=200),
        ),
    ]
