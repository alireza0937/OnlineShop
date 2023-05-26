from django.db import models
from django.utils.text import slugify
from account.models import User


class ArticleCategories(models.Model):
    title = models.CharField(max_length=200)
    url_title = models.CharField(max_length=200)
    is_active = models.BooleanField()

    class Meta:
        verbose_name_plural = 'ArticleCategories'

    def __str__(self):
        return self.title


class ArticleTags(models.Model):
    title = models.CharField(max_length=200)
    url_title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'ArticleTags'

    def __str__(self):
        return self.title


class Articles(models.Model):
    title = models.CharField(max_length=220)
    category = models.ForeignKey(ArticleCategories, on_delete=models.CASCADE)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(ArticleTags)
    banner = models.ImageField(upload_to='articles/')
    date = models.DateField(auto_now_add=True)
    text = models.TextField()
    is_active = models.BooleanField()
    slug = models.SlugField(unique=True, editable=False, db_index=True, max_length=200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Articles, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title


class ArticleComment(models.Model):
    title = models.CharField(max_length=220)
    parent_comment = models.ForeignKey('ArticleComment', on_delete=models.CASCADE, null=True, blank=True)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Articles, on_delete=models.CASCADE)
    message = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    is_span = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'ArticleComment'

    def __str__(self):
        return self.title
