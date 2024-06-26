# Generated by Django 5.0.4 on 2024-04-30 16:19

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='actors/', verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('tagline', models.CharField(default='', max_length=100, verbose_name='Слоган')),
                ('description', models.TextField(verbose_name='Описание')),
                ('poster', models.ImageField(upload_to='movies/', verbose_name='Постер')),
                ('year', models.PositiveSmallIntegerField(default=2019, verbose_name='Дата выхода')),
                ('country', models.CharField(max_length=30, verbose_name='Страна')),
                ('world_premiere', models.DateField(default=datetime.date.today, verbose_name='Примьера в мире')),
                ('budget', models.PositiveIntegerField(default=0, help_text='указывать сумму в долларах', verbose_name='Бюджет')),
                ('fees_in_usa', models.PositiveIntegerField(default=0, help_text='указывать сумму в долларах', verbose_name='Сборы в США')),
                ('fess_in_world', models.PositiveIntegerField(default=0, help_text='указывать сумму в долларах', verbose_name='Сборы в мире')),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('actors', models.ManyToManyField(related_name='film_actor', to='kino_site.actor', verbose_name='актеры')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kino_site.category', verbose_name='Категория')),
                ('directors', models.ManyToManyField(related_name='film_director', to='kino_site.actor', verbose_name='режиссер')),
                ('genres', models.ManyToManyField(to='kino_site.genre', verbose_name='жанры')),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.CharField(choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')], max_length=16)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kino_site.movie', verbose_name='фильм')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('date', models.DateTimeField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kino_site.comment', verbose_name='Родитель')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kino_site.movie', verbose_name='фильм')),
            ],
        ),
        migrations.CreateModel(
            name='MovieShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='ing/')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kino_site.movie')),
            ],
        ),
    ]
