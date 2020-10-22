from django.shortcuts import get_object_or_404, render
from .models import Todo
from django.contrib.auth.decorators import login_required
from .forms import TodoForm

# Create your views here.
@login_required
def index(request):
    todos = Todo.objects.all()

    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
    else:
        form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'todos/form.html', context)