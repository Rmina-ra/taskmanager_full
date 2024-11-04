# Generated by Django 5.1.2 on 2024-10-25 08:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название сортировки')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
            options={
                'verbose_name': 'Сортировка по',
                'verbose_name_plural': 'Сортировать по',
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название задачи')),
                ('customer', models.CharField(max_length=100, verbose_name='Имя заказчика')),
                ('deadline', models.CharField(max_length=100, verbose_name='Дедлайн')),
                ('difficulty', models.CharField(max_length=80, verbose_name='Сложность')),
                ('description', models.TextField(verbose_name='Описание задачи')),
                ('condition', models.TextField(verbose_name='Описание условия')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес заказа')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskmanager_app.category', verbose_name='Выберите сортировку')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]
