# Generated by Django 5.1.1 on 2024-10-15 11:07

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_alter_course_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='content_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Contenido del curso'),
        ),
        migrations.AddField(
            model_name='course',
            name='content_es',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Contenido del curso'),
        ),
        migrations.AddField(
            model_name='course',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Título del curso'),
        ),
        migrations.AddField(
            model_name='course',
            name='title_es',
            field=models.CharField(max_length=200, null=True, verbose_name='Título del curso'),
        ),
    ]