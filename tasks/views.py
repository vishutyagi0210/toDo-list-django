from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task
from .forms import TaskForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        queryset = Task.objects.all()
        task_submit = TaskForm
        tasks_dict = {'tasks': queryset , 'form': task_submit}
        return render(request , 'home.html' , tasks_dict)
    
def updateTask(request , pk):
    task = get_object_or_404(Task , id=pk)
    form = TaskForm(instance=task)
    
    if request.method == 'POST':
        task_update = TaskForm(request.POST , instance=task)
        if task_update.is_valid():
            task_update.save()
            return redirect('/')
    
    return render(request , 'update_task.html' , {'form':form})

def deleteTask(request , pk):
    item = get_object_or_404(Task , id=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    
    container = {'item':item}
    return render(request , 'delete.html' , container)