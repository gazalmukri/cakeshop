# Generated by Django 3.1.7 on 2021-06-03 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0003_cakes'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=255)),
                ('Name', models.CharField(max_length=255)),
                ('Phone', models.CharField(max_length=255)),
            ],
        ),
    ]