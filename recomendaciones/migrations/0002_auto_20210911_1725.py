# Generated by Django 3.2.5 on 2021-09-11 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recomendaciones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academicgroup',
            name='info_acad',
        ),
        migrations.DeleteModel(
            name='InfoAcademica',
        ),
        migrations.RemoveField(
            model_name='recreativeactivity',
            name='info_acad',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='info_acad',
        ),
        migrations.DeleteModel(
            name='AcademicGroup',
        ),
        migrations.DeleteModel(
            name='RecreativeActivity',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]