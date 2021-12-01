from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Task
from .forms import TaskForm

def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'app/task.html', {'task': task})

def list(request):
    tasks = Task.objects.all()
    return render(request, 'app/list.html', {'tasks': tasks})

def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')

    else:
        form = TaskForm()
        return render(request, 'app/addtask.html', {'form': form})

def yourName(request, name):
    return render(request, 'app/yourname.html', {'name': name })
