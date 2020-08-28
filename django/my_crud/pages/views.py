from django.shortcuts import render, redirect
from .models import Writing


def index(request):
    writings = Writing.objects.all()[::-1]
    context = {
        'writings': writings,
    }
    return render(request, 'pages/index.html', context)

def new(request):
    return render(request, 'pages/new.html')

def create(request):
    title = request.POST.get('title')
    if title == '':
        title = '<제목이 없습니다.>'
    content = request.POST.get('content')
    if content == '':
        content = '<내용이 없습니다.>'
    writing = Writing.objects.create(title=title, content=content)

    return redirect('pages:detail', writing.pk)

def detail(request, pk):
    writing = Writing.objects.get(pk=pk)
    context = {
        'writing': writing,
    }
    return render(request, 'pages/detail.html', context)

def edit(request, pk):
    writing = Writing.objects.get(pk=pk)
    if writing.title == '<제목이 없습니다.>':
        writing.title = ''
    if writing.content == '<내용이 없습니다.>':
        writing.content = ''
    context = {
        'writing': writing,
    }
    return render(request, 'pages/edit.html', context)

def update(request, pk):
    writing = Writing.objects.get(pk=pk)
    writing.title = request.POST.get('title')
    if writing.title == '':
        writing.title = '<제목이 없습니다.>'
    writing.content = request.POST.get('content')
    if writing.content == '':
        writing.content = '<제목이 없습니다.>'
    writing.save()
    return redirect('pages:detail', pk)

def delete(request, pk):
    writing = Writing.objects.get(pk=pk)
    if request.method == 'POST':
        writing.delete()
    print(request.method)
    return redirect('pages:index')