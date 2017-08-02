# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('image', models.FileField(null=True, upload_to=b'', blank=True)),
                ('phone', models.CharField(max_length=4, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('returning', models.TextField(blank=True)),
                ('user', models.CharField(max_length=50, null=True)),
                ('site_phone', models.CharField(max_length=20, null=True, blank=True)),
                ('site', models.CharField(max_length=100, null=True, blank=True)),
                ('schedule', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('division', models.ForeignKey(to='checkout.Division')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desc', models.CharField(max_length=100)),
                ('statusId', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='group',
            field=models.ForeignKey(to='checkout.Group'),
        ),
        migrations.AddField(
            model_name='employee',
            name='section',
            field=models.ForeignKey(to='checkout.Section'),
        ),
        migrations.AddField(
            model_name='employee',
            name='status',
            field=models.ForeignKey(to='checkout.Status'),
        ),
    ]
