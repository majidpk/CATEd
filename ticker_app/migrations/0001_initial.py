# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeTicker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange_id', models.IntegerField()),
                ('pair_id', models.IntegerField()),
                ('high', models.DecimalField(decimal_places=15, max_digits=30)),
                ('last', models.DecimalField(decimal_places=15, max_digits=30)),
                ('low', models.DecimalField(decimal_places=15, max_digits=30)),
                ('bid', models.DecimalField(decimal_places=15, max_digits=30)),
                ('ask', models.DecimalField(decimal_places=15, max_digits=30)),
                ('base_volume', models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True)),
                ('percent_change', models.DecimalField(decimal_places=8, default=0, max_digits=10)),
                ('date_time', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Данные тикера',
                'verbose_name_plural': 'Данные тикеров',
            },
        ),
    ]
