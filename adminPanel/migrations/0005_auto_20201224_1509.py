# Generated by Django 3.1.2 on 2020-12-24 09:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0004_auto_20201209_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='negativeMarksInput',
        ),
        migrations.AlterField(
            model_name='test',
            name='createdOn',
            field=models.DateField(default=datetime.datetime(2020, 12, 24, 15, 9, 33, 342210), verbose_name='Posted on'),
        ),
    ]
