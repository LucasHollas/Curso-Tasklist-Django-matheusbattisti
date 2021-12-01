from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Task

def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'app/task.html', {'task': task})

def list(request):
    tasks = Task.objects.all()
    return render(request, 'app/list.html', {'tasks': tasks})

def yourName(request, name):
    return render(request, 'app/yourname.html', {'name': name })
