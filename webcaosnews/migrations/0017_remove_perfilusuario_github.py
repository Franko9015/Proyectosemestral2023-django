# Generated by Django 4.2.2 on 2023-06-29 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webcaosnews', '0016_alter_perfilusuario_facebook_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfilusuario',
            name='github',
        ),
    ]