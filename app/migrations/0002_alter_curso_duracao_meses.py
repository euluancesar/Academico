# Generated by Django 5.2.1 on 2025-05-19 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='duracao_meses',
            field=models.IntegerField(verbose_name='Duração em meses'),
        ),
    ]
