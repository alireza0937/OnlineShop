# Generated by Django 4.2.1 on 2023-05-22 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_articlecomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecomment',
            name='parent_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article.articlecomment'),
        ),
    ]