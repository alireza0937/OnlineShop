# Generated by Django 4.2.1 on 2023-05-29 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_productvisit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.BigIntegerField(max_length=250),
        ),
    ]
