# Generated by Django 4.0.4 on 2022-05-22 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newscreation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newslink',
            name='source',
            field=models.CharField(max_length=255, null=True, verbose_name='Источник'),
        ),
    ]
