# Generated by Django 3.0.3 on 2020-02-21 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20200221_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='month',
            field=models.CharField(default='', max_length=15),
        ),
    ]
