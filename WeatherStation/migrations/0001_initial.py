# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('timeStamp', models.DateTimeField()),
                ('recordNum', models.IntegerField(primary_key=True, serialize=False)),
                ('battAvg', models.DecimalField(decimal_places=2, max_digits=4)),
                ('pTempCAvg', models.DecimalField(decimal_places=2, max_digits=4)),
                ('airTCAvg', models.DecimalField(decimal_places=2, max_digits=4)),
                ('rH', models.DecimalField(decimal_places=2, max_digits=4)),
                ('slrkW', models.DecimalField(decimal_places=2, max_digits=4)),
                ('slrMJTot', models.DecimalField(decimal_places=6, max_digits=8)),
                ('wSMs', models.DecimalField(decimal_places=3, max_digits=6)),
                ('windDir', models.DecimalField(decimal_places=1, max_digits=5)),
                ('pARDen', models.DecimalField(decimal_places=1, max_digits=5)),
                ('pARTotTot', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bPMmHg', models.DecimalField(decimal_places=1, max_digits=6)),
                ('rainMmTot', models.IntegerField()),
            ],
            options={
                'managed': True,
                'ordering': ['-recordNum'],
            },
        ),
    ]