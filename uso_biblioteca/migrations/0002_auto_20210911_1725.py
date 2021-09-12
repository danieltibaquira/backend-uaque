# Generated by Django 3.2.5 on 2021-09-11 22:25

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uso_biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repores',
            name='description',
            field=models.CharField(default='No description', max_length=255),
        ),
        migrations.AddField(
            model_name='repores',
            name='format',
            field=models.CharField(default='No format', max_length=255),
        ),
        migrations.AddField(
            model_name='repores',
            name='subjects',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255), default='no subject', size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tranrepo',
            name='typeUse',
            field=models.CharField(default='No type use', max_length=255),
        ),
    ]