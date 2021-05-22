# Generated by Django 2.2.3 on 2020-02-23 15:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_auto_20200223_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='level_flag',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)]),
        ),
    ]
