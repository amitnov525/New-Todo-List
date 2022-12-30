from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from main.models import Task
from django.urls import reverse_lazy

# Create your views here.
class TodoTask(LoginRequiredMixin,ListView):
    model=Task
    context_object_name='tasks'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['tasks']=context['tasks'].filter(user=self.request.user)
        context['count']=context['tasks'].filter(completed=False).count()
        search_input=self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks']=context['tasks'].filter(title__startswith=search_input)
        context['serach_input']=search_input
        return context

class TodoTask_detail(LoginRequiredMixin,DetailView):
    model=Task
    context_object_name='task' 

class CreateTask(LoginRequiredMixin,CreateView):
    model=Task
    fields=['title','description','completed']
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    success_url=reverse_lazy('tasks')

class UpdateTask(LoginRequiredMixin,UpdateView):
    model=Task
    fields=['title','description','completed']
    success_url=reverse_lazy('tasks')

class DeleteTask(LoginRequiredMixin,DeleteView):
    model=Task
    context_object_name='task'
    success_url=reverse_lazy('tasks')

class Login_user(LoginView):
    template_name='main/login.html'
    fields='__all__'
    redirect_authenticated_user=True 

    def get_success_url(self):
        return reverse_lazy('tasks')

class UserRegister(FormView):
    template_name='main/register.html'
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('tasks')
    def form_valid(self,form):
        user=form.save()
        if user is not None:
            login(self.request,user)
            return super().form_valid(form)
    
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super().get(*args,**kwargs)
    

