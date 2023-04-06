from django.shortcuts import render, redirect
from .models import Article
from django.utils import timezone
# Create your views here.
def info(request):
    return render(request, 'info.html')

def project(request):
    return render(request, 'project.html')

def write_new(request):
    if request.method == 'POST':
        
        print(request.POST)

        new_article = Article.objects.create(
            article_category = request.POST['article_category'],
            title = request.POST['title'],
            content = request.POST['content'],
            written_time = timezone.localtime()
        )
        return redirect('list')

    return render(request, 'write_new.html')

def list(request, category=None):
    cate_list = Article.category
    cates = []
    num = []
    for cate in cate_list:
        cate = cate[0]
        print(cate)
        cates.append(cate)
        num.append(Article.objects.filter(article_category=cate).count())

    cate_num = zip(cates, num)

    if request.method == 'POST' and request.POST['category'] != 'category':
        print(request.POST)
        articles = Article.objects.filter(article_category=request.POST['category'])
        return render(request, 'list.html', {'articles':articles, 'cate_num':cate_num})
    elif category != None:
        print(request.POST)
        articles = Article.objects.filter(article_category=category)
        return render(request, 'list.html', {'articles':articles, 'cate_num':cate_num})
    
    articles = Article.objects.all()
    return render(request, 'list.html', {'articles': articles, 'cate_num':cate_num})
    
def detail(request, id):
    article = Article.objects.get(id=id)
    article = {'article':article}
    return render(request, 'detail.html', article)

def category(request):
    return render(request, 'category.html')