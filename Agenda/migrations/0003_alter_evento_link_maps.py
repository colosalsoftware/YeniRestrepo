# Generated by Django 4.2.5 on 2023-11-05 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agenda', '0002_evento_link_maps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='link_maps',
            field=models.CharField(max_length=500),
        ),
    ]
