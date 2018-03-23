# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-16 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProtocolElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('description', models.CharField(max_length=300)),
                ('removed', models.BooleanField(default=False)),
                ('hash', models.CharField(max_length=50, unique=True)),
                ('nextElement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='protocol_element.ProtocolElement')),
            ],
        ),
    ]