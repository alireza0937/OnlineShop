from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from article.forms import CommentsForm
from article.models import Articles, ArticleComment, ArticleCategories


class BlogListView(ListView):
    template_name = 'article/all_articles.html'
    model = Articles
    context_object_name = 'articles'
    paginate_by = 3

    def get_queryset(self, *args, **kwargs):
        query = super(BlogListView, self).get_queryset()
        tag = self.kwargs.get('tag')
        cat = self.kwargs.get('cat')
        if tag is not None:
            query = query.filter(tags__url_title__contains=tag).all()
        if cat is not None:
            query = query.filter(category__url_title__iexact=cat).all()
        return query


class BlogDetailView(DetailView):
    template_name = 'article/article_details.html'
    model = Articles
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data()
        context['forms'] = CommentsForm()
        article_id: Articles = self.kwargs.get('pk')
        context['comments'] = \
            ArticleComment.objects.annotate(comment_count=Count('blog_id')).filter(is_span=False,
                                                                                   blog_id=article_id).all()
        return context

    def post(self, request: HttpRequest, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            message = request.POST.get('message')
            message_title = request.POST.get('title')
            user_comment = ArticleComment(title=message_title,
                                          auther_id=request.user.id,
                                          blog_id=pk,
                                          message=message)
            user_comment.save()
            return redirect(reverse("blog-detail-page", args=pk))

        return render(request, 'article/article_details.html', context={
            'form': CommentsForm
        })


def article_categories(request: HttpRequest):
    all_categories = ArticleCategories.objects.filter(is_active=True).all()
    return render(request, 'article/article_components/categories.html', context={
        'categories': all_categories
    })


def recent_post(request: HttpRequest):
    most_recent_articles = Articles.objects.all().order_by('-date')[:4]
    return render(request, 'article/article_components/recent_post.html', context={
        'recent': most_recent_articles
    })
