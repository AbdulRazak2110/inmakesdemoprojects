# Generated by Django 4.1.4 on 2023-01-06 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taskapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1996-10-25'),
            preserve_default=False,
        ),
    ]