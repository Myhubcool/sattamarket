# Generated by Django 2.2.6 on 2019-11-06 01:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_auto_20191105_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='userwallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useramt', models.CharField(max_length=20)),
                ('userid', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='umanagedata',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 5, 17, 51, 35, 978960)),
        ),
    ]
