# Generated by Django 3.0.3 on 2021-03-25 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_merge_20210325_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='phone_number',
            field=models.BigIntegerField(),
        ),
    ]