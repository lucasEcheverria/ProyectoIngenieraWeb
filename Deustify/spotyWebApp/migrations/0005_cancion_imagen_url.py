# Generated by Django 5.1.2 on 2024-10-31 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotyWebApp', '0004_artista_imagen_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancion',
            name='imagen_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]