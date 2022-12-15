from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic import View, DetailView, CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from .models import Task

class CustomLogin(LoginView):
    template_name="main/login.html"
    fields="__all__"
    redirect_authenticated_user= True
    
    def get_success_url(self):
        return reverse_lazy('tasks')


class taskList(LoginRequiredMixin, ListView):
    
    model = Task
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        context['count'] = context['tasks'].filter(complete = False).count()
        return context
    
class taskDetail(LoginRequiredMixin, DetailView):
    
    model = Task
    context_object_name = 'task'
    
class taskCreate(LoginRequiredMixin, CreateView):
    
    model = Task
    context_object_name = 'task'
    #fields = ['title', 'description', 'complete']
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(taskCreate, self).form_valid(form)
    
class taskUpdate(LoginRequiredMixin, UpdateView):
    
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class taskDelete(LoginRequiredMixin, DeleteView):
    
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')