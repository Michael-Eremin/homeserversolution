# Generated by Django 4.0.4 on 2022-05-22 13:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, null=True, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='NewsLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название новости')),
                ('description', models.TextField(blank=True, verbose_name='Предисловие')),
                ('img_link', models.TextField(validators=[django.core.validators.URLValidator()], verbose_name='Представление')),
                ('img_path', models.ImageField(upload_to='images', verbose_name='Картинка')),
                ('content_link', models.TextField(validators=[django.core.validators.URLValidator()], verbose_name='Содержание')),
                ('date_published', models.DateField(verbose_name='Дата публикации')),
                ('date_added', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newscreation.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
