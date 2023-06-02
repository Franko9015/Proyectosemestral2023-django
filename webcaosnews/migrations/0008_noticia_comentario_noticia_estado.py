# Generated by Django 4.2 on 2023-06-02 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcaosnews', '0007_remove_noticia_foto_noticia_fotos_noticia_miniatura_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='comentario',
            field=models.CharField(default='se rechazo por un motivo', max_length=200),
        ),
        migrations.AddField(
            model_name='noticia',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('aprobado', 'Aprobado'), ('rechazado', 'Rechazado')], default='pendiente', max_length=10),
        ),
    ]
