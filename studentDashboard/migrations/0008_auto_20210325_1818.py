# Generated by Django 3.0.3 on 2021-03-25 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentDashboard', '0007_exam_history_is_test_given'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time_tracker',
            name='time_left',
            field=models.CharField(max_length=100, null=True),
        ),
    ]