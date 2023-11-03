# Generated by Django 4.2.5 on 2023-11-03 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animalito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='photos/Animalitos')),
                ('nombre', models.CharField(max_length=200)),
                ('edad', models.CharField(max_length=200)),
                ('raza', models.CharField(max_length=200)),
                ('tamaño', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('esta_disponible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Animalito',
                'verbose_name_plural': 'Animalitos',
            },
        ),
    ]