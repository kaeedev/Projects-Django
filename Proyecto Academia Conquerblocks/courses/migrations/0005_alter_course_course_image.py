# Generated by Django 5.1.1 on 2024-09-16 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_image',
            field=models.ImageField(blank=True, null=True, upload_to='courses/images/', verbose_name='Portada del curso'),
        ),
    ]