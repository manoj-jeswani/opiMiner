# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-10 05:25
from __future__ import unicode_literals

from django.db import migrations, models
import logical.models


class Migration(migrations.Migration):

    dependencies = [
        ('logical', '0003_temporarydetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search_Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kw', models.CharField(blank=True, max_length=250)),
                ('sres', logical.models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
