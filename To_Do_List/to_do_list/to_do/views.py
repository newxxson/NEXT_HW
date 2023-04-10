from django.shortcuts import render, redirect
from .models import To_Do_Element
import datetime
from django.utils.timezone import make_aware
# Create your views here.
def add_new(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST['content']
        due_date = request.POST['due_date']
        due_date = datetime.datetime.strptime(due_date, "%Y-%m-%dT%H:%M")
        due_date = make_aware(due_date)

        new_post = To_Do_Element.objects.create(
            title = title,
            content = content,
            due_date = due_date,
            done = False
        )
        return redirect('home')

    post = {}

    current_time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
    max_time = current_time.replace(current_time[:4], str(int(current_time[:4])+1))
    print(max_time)
    post['current_time'] = current_time
    post['max_time'] = max_time

    return render(request, 'add_new.html', post)

def home(request):
    to_do_list = To_Do_Element.objects.all().order_by('due_date')
    
    return render(request, 'home.html', {'to_do_list' : to_do_list})

def detail(request, pk):
    to_do = To_Do_Element.objects.get(pk=pk)

    return render(request, 'detail.html', {"to_do": to_do})


def delete(request, post_pk):
    post = To_Do_Element.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')

def edit(request, pk):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        due_date = request.POST['due_date']
        due_date = datetime.datetime.strptime(due_date, "%Y-%m-%dT%H:%M")
        due_date = make_aware(due_date)

        To_Do_Element.objects.filter(pk=pk).update(
            title=title,
            content=content,
            due_date=due_date
        )
        return redirect('home')
    
    to_do = To_Do_Element.objects.get(pk=pk)
    current_time = to_do.due_date.strftime("%Y-%m-%dT%H:%M")
    max_time = current_time.replace(current_time[:4], str(int(current_time[:4])+1))
    return render(request, 'edit.html', {'to_do':to_do, 'current_time': current_time,'max_time':max_time})

def done(request, pk):

    element = To_Do_Element.objects.get(pk=pk)

    post = To_Do_Element.objects.filter(pk=pk)

    if element.done:
        post.update(
            done = False
        )
    else:
        post.update(
            done = True
        )

    return redirect('home')