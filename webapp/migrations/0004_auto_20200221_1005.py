# Generated by Django 3.0.3 on 2020-02-21 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20200221_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='month',
            field=models.CharField(default='Add Month', max_length=15),
        ),
    ]
