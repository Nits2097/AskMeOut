# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-10 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180128_0711'),
    ]

    operations = [
        migrations.CreateModel(
            name='call',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('callid', models.IntegerField(max_length=100)),
                ('date', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=10)),
                ('sentiment', models.CharField(max_length=10)),
                ('summary', models.CharField(max_length=500)),
                ('service_provider', models.CharField(max_length=100)),
                ('intent', models.CharField(max_length=100)),
                ('rating', models.IntegerField(max_length=10)),
                ('ccid', models.IntegerField(max_length=20)),
            ],
        ),
    ]
