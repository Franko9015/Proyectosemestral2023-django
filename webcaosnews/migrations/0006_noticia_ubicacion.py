# Generated by Django 4.2 on 2023-05-10 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcaosnews', '0005_noticia_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='Ubicacion',
            field=models.CharField(default='Desconocido', max_length=15),
        ),
    ]
