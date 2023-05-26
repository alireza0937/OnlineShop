# Generated by Django 4.2.1 on 2023-05-17 10:03
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('response', models.TextField(blank=True)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
            options={
                'db_table': 'ContactUs',
            },
        ),
    ]