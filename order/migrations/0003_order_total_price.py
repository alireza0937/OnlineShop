# Generated by Django 4.2.1 on 2023-06-06 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_orderdetail_price_orderdetail_final_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
