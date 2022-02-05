from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm


def home(request):
    pi = Task.objects.order_by("-date_time")
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    form = TaskForm()
    return render(request, 'firstapp/home.html', {'form': form, 'pi': pi})


def delete(request, id):
    pi = Task.objects.get(pk=id)
    pi.delete()
    return redirect('/')
