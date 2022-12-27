from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic import View, DetailView, CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task, Team

class CustomLogin(LoginView):
    template_name="main/login.html"
    fields="__all__"
    redirect_authenticated_user= True
    
    def get_success_url(self):
        return reverse_lazy('tasks')

class RegisterPage(FormView):
    
    template_name='main/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user= True
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(self.request,**kwargs)
    

class taskList(LoginRequiredMixin, ListView):
    
    model = Task
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        context['count'] = context['tasks'].filter(complete = False).count()
        
        search_input = self.request.GET.get("search-area") or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)   
            
        context['search_input'] = search_input
                 
        return context
    
class taskDetail(LoginRequiredMixin, DetailView):
    
    model = Task
    context_object_name = 'task'
    
class taskCreate(LoginRequiredMixin, CreateView):
    
    model = Task
    context_object_name = 'task'
    #fields = ['title', 'description', 'complete']
    fields = ['title', 'description', 'urgent','complete']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(taskCreate, self).form_valid(form)
    
class taskUpdate(LoginRequiredMixin, UpdateView):
    
    model = Task
    fields = ['title','description','urgent','complete']
    success_url = reverse_lazy('tasks')
    
class taskDelete(LoginRequiredMixin, DeleteView):
    
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    
class teamList(LoginRequiredMixin, ListView):
    model = Team
    context_object_name = 'teams'
    template_name= 'team_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = context['teams'].filter(member = self.request.user)
        
        return context