from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    context = {
        'task': tasks,
    }
    return render(request, 'task/task_list.html', context)