# Generated by Django 4.2.7 on 2023-11-08 16:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joke', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joke',
            name='joke_start_data',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 8, 19, 34, 12, 651551), null=True, verbose_name='Дата создания'),
        ),
    ]
