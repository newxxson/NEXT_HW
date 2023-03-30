from django.shortcuts import render

# Create your views here.
def hello(request):

    return render(request, 'hello.html')

def count(request):
    return render(request, 'count.html')

def result(request):
    text=request.POST['text']
    total_len = len(text)
    stripped = len(text.replace(' ', ''))
    return render(request, 'result.html', {'total_len':total_len, 'text':text, 'stripped':stripped})