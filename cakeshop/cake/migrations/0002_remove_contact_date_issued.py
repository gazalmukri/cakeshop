# Generated by Django 3.1.7 on 2021-05-26 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='date_issued',
        ),
    ]
