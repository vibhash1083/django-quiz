# Generated by Django 2.2.3 on 2020-02-23 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20200223_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='level_flag',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
        ),
    ]
