# Generated by Django 2.2 on 2019-04-29 15:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 4, 29, 18, 11, 17, 180541)),
        ),
    ]
