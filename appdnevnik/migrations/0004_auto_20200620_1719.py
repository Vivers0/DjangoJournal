# Generated by Django 2.1.7 on 2020-06-20 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdnevnik', '0003_auto_20200620_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='example',
            name='homework',
            field=models.TextField(blank=True, verbose_name='Домашнее задание'),
        ),
        migrations.AlterField(
            model_name='example',
            name='cabinet',
            field=models.CharField(blank=True, max_length=300, verbose_name='Кабинет'),
        ),
    ]
