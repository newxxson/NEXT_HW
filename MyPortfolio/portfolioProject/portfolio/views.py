from django.shortcuts import render, redirect
from .models import Article, Comment, Reply
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
    print('still working')
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
    print("rtttt")
    articles = Article.objects.all()
    return render(request, 'list.html', {'articles': articles, 'cate_num':cate_num})
    
def detail(request, id):
    article = Article.objects.get(id=id)
    print("asdfasdfasdf")

    if request.method == 'POST':
        print('posting')
        if 'comment' in request.POST:
            print('comment')
            content= request.POST['comment']
            Comment.objects.create(
                article = article,
                content = content
            )
            
        elif 'reply' in request.POST:
            print('reply')
            content = request.POST['reply']
            comment = Comment.objects.get(id=request.POST['comment_id'])
            Reply.objects.create(
                comment = comment,
                content = content
            )
        else:
            print('error occured while obtaining target')
        return redirect('detail', id)

    article = {'article':article}
    return render(request, 'detail.html', article)

def category(request):
    return render(request, 'category.html')

def delete_comment(request, article_id, comment_id):
    comment = Comment.objects.get(id = comment_id)
    comment.delete()

    return redirect('detail', article_id)

def delete_reply(request, article_id, reply_id):
    reply = Reply.objects.get(id=reply_id)
    reply.delete()

    return redirect('detail', article_id)