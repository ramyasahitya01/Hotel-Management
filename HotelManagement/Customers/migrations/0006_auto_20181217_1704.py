# Generated by Django 2.1.4 on 2018-12-17 11:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0005_auto_20181217_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customervisits',
            name='assigned_room',
        ),
        migrations.AlterField(
            model_name='customers',
            name='room_assigned_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 17, 17, 4, 36, 20190), editable=False),
        ),
        migrations.DeleteModel(
            name='CustomerVisits',
        ),
    ]
