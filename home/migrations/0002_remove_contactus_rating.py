# Generated by Django 4.2.1 on 2023-05-17 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='rating',
        ),
    ]
