from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import Tasks
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from .forms import TaskCreateForm

# Create your views here.
class TaskEdit(UpdateView):
    model = Tasks
    template_name = 'items/taskedit.html'
    fields = ['title', 'description',]
    success_url = reverse_lazy('users:home')

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print(form.errors)
        print('not saving')
        return super().form_invalid(form)


class CreateTask(CreateView):
    model = Tasks
    template_name = 'items/taskcreate.html'
    fields = ['title','description']
    success_url = reverse_lazy('users:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
   

class TaskDetail(DetailView):
    model = Tasks
    template_name = 'items/taskdetail.html'
    context_object_name = 'task'







    

