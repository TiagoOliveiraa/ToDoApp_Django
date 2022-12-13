from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Task
from django.urls import reverse_lazy
from django.views.generic import View, DetailView, CreateView, UpdateView, DeleteView

def test(request):
    return HttpResponse("The view is working")

class taskList(ListView):
    
    model = Task
    context_object_name = 'tasks'
    
class taskDetail(DetailView):
    
    model = Task
    context_object_name = 'task'
    
class taskCreate(CreateView):
    
    model = Task
    context_object_name = 'task'
    #fields = ['title', 'description', 'complete']
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class taskUpdate(UpdateView):
    
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class taskDelete(DeleteView):
    
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')