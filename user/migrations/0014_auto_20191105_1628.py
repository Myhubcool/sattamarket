# Generated by Django 2.2.6 on 2019-11-06 00:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20191105_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='umanagedata',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 5, 16, 28, 22, 98508)),
        ),
    ]
