from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from Accounts.models import Account
from django.contrib import auth

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})


@login_required(login_url='Accounts:unauth')
def new(request):
    if request.method == "POST":
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.user
        )
        user = Account.objects.get(pk=request.user.pk)
        user.total_post += 1
        return redirect('Blog:detail', new_post.pk)
    return render(request, 'new.html')

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == "POST":
        text = request.POST['content']
        new_comment = Comment.objects.create(
            post = post,
            comment = text,
            author = request.user
        )
        redirect('Blog:detail', post.pk)

    return render(request, 'detail.html', {'post':post})

@login_required(login_url='Accounts:unauth')
def update(request,	post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(
        title = request.POST['title'],
        content = request.POST['content']
        )
        return redirect('Blog:detail',	post_pk)
    return render(request,	'update.html',	{'post':post})

def delete(request,	post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('Blog:home')

def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('Blog:detail', post_pk)

