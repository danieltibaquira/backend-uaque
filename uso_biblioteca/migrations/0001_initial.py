# Generated by Django 3.2.6 on 2021-09-02 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AzRes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('idResource', models.CharField(max_length=255)),
                ('theme', models.CharField(max_length=255)),
                ('dateCreated', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('repo', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AzUse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('idUser', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LibRes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('idResource', models.CharField(max_length=255)),
                ('theme', models.CharField(max_length=255)),
                ('dateCreated', models.CharField(max_length=255)),
                ('copies', models.IntegerField()),
                ('typeRes', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LibUse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('idUser', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RepoRes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idResource', models.CharField(max_length=255)),
                ('theme', models.CharField(max_length=255)),
                ('dateCreated', models.CharField(max_length=255)),
                ('faculty', models.CharField(max_length=255)),
                ('program', models.CharField(max_length=255)),
                ('repo', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RepoUse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('idUser', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TranRepo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idResource', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('theme', models.CharField(max_length=255)),
                ('repoUse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uso_biblioteca.repouse')),
            ],
        ),
        migrations.CreateModel(
            name='TranLib',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('idResource', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('theme', models.CharField(max_length=255)),
                ('libUse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uso_biblioteca.libuse')),
            ],
        ),
        migrations.CreateModel(
            name='TranAz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('idResource', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('theme', models.CharField(max_length=255)),
                ('typeUse', models.CharField(max_length=255)),
                ('azUse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uso_biblioteca.azuse')),
            ],
        ),
    ]
