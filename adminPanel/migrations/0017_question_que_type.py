# Generated by Django 3.1.2 on 2021-03-12 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0016_auto_20210303_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='que_type',
            field=models.BooleanField(default=True),
        ),
    ]