# Generated by Django 3.0.5 on 2020-04-26 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stays', '0003_auto_20200416_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stay',
            name='plus',
        ),
        migrations.RemoveField(
            model_name='stay',
            name='second_image',
        ),
        migrations.RemoveField(
            model_name='stay',
            name='third_image',
        ),
    ]