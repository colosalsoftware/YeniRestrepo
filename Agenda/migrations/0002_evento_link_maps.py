# Generated by Django 4.2.5 on 2023-11-05 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agenda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='link_maps',
            field=models.CharField(default='https', max_length=500),
        ),
    ]
