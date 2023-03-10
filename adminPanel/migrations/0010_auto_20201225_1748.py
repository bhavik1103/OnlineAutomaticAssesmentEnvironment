# Generated by Django 3.0 on 2020-12-25 12:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0009_auto_20201225_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='option1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='option2',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='option3',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='option4',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='test',
            name='createdOn',
            field=models.DateField(default=datetime.datetime(2020, 12, 25, 17, 48, 24, 558463), verbose_name='Posted on'),
        ),
    ]
