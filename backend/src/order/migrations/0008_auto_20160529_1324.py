# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-29 06:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20160526_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='food_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.FoodItem', verbose_name='Блюдо'),
        ),
        migrations.AlterField(
            model_name='gift',
            name='requirement',
            field=models.PositiveIntegerField(verbose_name='Требование'),
        ),
    ]
