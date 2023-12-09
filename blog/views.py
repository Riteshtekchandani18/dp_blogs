
from django.shortcuts import render, redirect

from django.core.paginator import Paginator
from .models import Article, Topic
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home_view(request):

    articles_list = Article.objects.all()
    topic_list = Topic.objects.all()
    paginator = Paginator(articles_list, 12)
    page = request.GET.get('p', 1)
    articles = paginator.get_page(page)
    ctx={
        'articles':articles,
        'topic': topic_list,    }
    return render(request, 'blog/home.html',ctx)

@login_required
def add_view(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        topic = request.POST.get('topic')
        image = request.FILES.get('image')
        author = request.user
        if len(title)<3: 
            messages.error(request, 'Title must be at least 3 characters')
            return redirect ('add')
        if len (content)< 50:
            messages.error(request, 'content must be at least 50 cahracters')
            return redirect('add')
        if not image :
            messages.error(request, 'Image is required')
            return redirect('add')
        article = Article(title=title,
                          image =image,
                          content=content,
                          topic=topic,
                          author=author)
        article.save()
        messages.success(request, 'Articles created successfully.')   
        return redirect ('my_articles')
    return render(request, 'blog/add.html')

@login_required
def my_articles(request):
    article_list = Article.objects.filter(author = request.user)
    paginator = Paginator(article_list, 12)
    page = request.GET.get('p' ,1)
    ctx = {'articles' : paginator.get_page(page)}
    return render(request, 'blog/my_articles.html',ctx)

@login_required
def inc_like(request ,id):
    article = Article.objects.get(id=id)
    article.likes += 1
    article.save()
    return redirect('detail', id=id)

def details(request , id):
    ctx = {'article': Article.objects.get(id=id)}
    return render(request, 'blog/detail.html')

@login_required         
def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    messages.success(request, 'Articles delete succesfully')
    return redirect('my_articles')

@login_required
def edit(request, id):
    return render(request, 'blog/home.html')
        
# Create your views here.
