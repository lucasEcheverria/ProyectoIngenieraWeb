# Generated by Django 5.1.2 on 2024-10-28 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotyWebApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]