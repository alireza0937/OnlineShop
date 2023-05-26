# Generated by Django 4.2.1 on 2023-05-17 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url_title', models.CharField(max_length=200)),
                ('is_active', models.BooleanField()),
            ],
            options={
                'db_table': 'ProductsBrand',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url_title', models.CharField(max_length=200)),
                ('is_active', models.BooleanField()),
            ],
            options={
                'db_table': 'ProductsCategories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='product/')),
                ('short_descriptions', models.CharField(db_index=True, max_length=500, null=True)),
                ('price', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('slug', models.SlugField(editable=False, max_length=200, unique=True)),
                ('is_new', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productbrand')),
                ('category', models.ManyToManyField(to='product.productcategory')),
            ],
            options={
                'db_table': 'Products',
            },
        ),
    ]
