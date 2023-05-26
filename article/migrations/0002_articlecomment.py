# Generated by Django 4.2.1 on 2023-05-22 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220)),
                ('message', models.TextField()),
                ('create_date', models.DateField(auto_now_add=True)),
                ('is_span', models.BooleanField(default=True)),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.articles')),
                ('parent_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.articlecomment')),
            ],
            options={
                'verbose_name_plural': 'ArticleComment',
            },
        ),
    ]
