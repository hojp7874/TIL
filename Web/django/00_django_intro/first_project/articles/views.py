# django import style guide
# 1. standart library
# 2. 3rd party
# 3. Django
# 4. local django
import random  #=> 3.
from django.shortcuts import render #=> 5.

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')


def dinner(request):
    menus = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menus)
    context = {
        'pick': pick,
    }
    return render(request, 'articles/dinner.html', context)

def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/hello.html', context)

def dtl_practice(request):
    menus = ['짜장면', '탕수육', '짬뽕']
    empty_list = []
    my_sentence = '주동이는 유학파야! 언어는 주동이한테 물어봐!'
    context = {
        'menus': menus,
        'empty_list': empty_list,
        'my_sentence': my_sentence,
    }
    return render(request, 'articles/dtl_practice.html', context)

def throw(request):
    return render(request, 'articles/throw.html')
    
def catch(request):
    
    return render(request, 'articles/catch.html')