# Generated by Django 4.2.2 on 2023-06-29 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webcaosnews', '0017_remove_perfilusuario_github'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuario',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL),
        ),
    ]
