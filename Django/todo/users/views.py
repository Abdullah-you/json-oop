from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignupForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import FormView
from items.models import Tasks
from django.views.generic import ListView


# Create your views here
def index(request):
    return render(request, 'users/index.html')

class SignupView(FormView):
    form_class = SignupForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:index')

    def form_valid(self,form):
        user = form.save()
        return super().form_valid(form)
    
class SignInView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/signin.html'
    success_url = reverse_lazy('users:home')

class Home(ListView):
    model = Tasks
    template_name = 'users/home.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user)
    #return render(request, 'users/home.html')

def logoutView(request):
    logout(request)
    return redirect('users:index')
