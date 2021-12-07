from django.core import paginator
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import TaskForm

@login_required
def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'app/task.html', {'task': task})

@login_required
def taskList(request):

    search = request.GET.get('search')

    if search:

        tasks = Task.objects.filter(title__icontains=search, user = request.user)

    else:

        tasks_list = Task.objects.all().filter(user = request.user)

        paginator = Paginator(tasks_list, 5)

        page = request.GET.get('page')

        tasks = paginator.get_page(page)

    return render(request, 'app/list.html', {'tasks': tasks})

@login_required
def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.user = request.user
            task.save()
            return redirect('/')

    else:
        form = TaskForm()
        return render(request, 'app/addtask.html', {'form': form})

@login_required
def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)

        if(form.is_valid()):
            task.save()
            return redirect('/')    
        else:
             return render(request, 'app/edittask.html', {'form': form, 'task': task})
    else:
        return render(request, 'app/edittask.html', {'form': form, 'task': task})

@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso.')

    return redirect('/')

@login_required
def changeStatus(request, id):
    task = get_object_or_404(Task, pk=id)

    if(task.done=='doing'):
        task.done = 'done'
    else:
        task.done = 'doing'

    task.save()

    return redirect('/')


def yourName(request, name):
    return render(request, 'app/yourname.html', {'name': name })
