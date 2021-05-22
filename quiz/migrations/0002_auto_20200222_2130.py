# Generated by Django 2.2.3 on 2020-02-22 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='is_repeated',
        ),
        migrations.AddField(
            model_name='questions',
            name='is_repeated',
            field=models.BooleanField(default=False, help_text='Is this a repeated question?'),
        ),
    ]
