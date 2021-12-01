from django.shortcuts import render
from django.http import HttpResponse

def list(request):
    return render(request, 'app/list.html')

def yourName(request, name):
    return render(request, 'app/yourname.html', {'name': name })
