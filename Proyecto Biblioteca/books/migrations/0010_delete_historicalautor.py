# Generated by Django 5.1.1 on 2024-09-24 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_alter_libro_idioma'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HistoricalAutor',
        ),
    ]
