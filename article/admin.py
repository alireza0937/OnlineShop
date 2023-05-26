from django.contrib import admin
from article.models import Articles, ArticleCategories, ArticleTags, ArticleComment

admin.site.register(Articles)
admin.site.register(ArticleCategories)
admin.site.register(ArticleTags)
admin.site.register(ArticleComment)
