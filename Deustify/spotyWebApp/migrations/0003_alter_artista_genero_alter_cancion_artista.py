# Generated by Django 5.1.2 on 2024-10-29 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotyWebApp', '0002_alter_genero_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artistas', to='spotyWebApp.genero'),
        ),
        migrations.AlterField(
            model_name='cancion',
            name='artista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='canciones', to='spotyWebApp.artista'),
        ),
    ]
