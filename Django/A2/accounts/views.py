from django.forms.models import BaseModelForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from .forms import SignupForm
from django.views.generic import FormView, UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache



# Create your views here.
class UserCreate(FormView):
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self,form):
        user = form.save()
        return super().form_valid(form)


class UserLogin(LoginView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('accounts:profile')


def LogoutView(request):
    logout(request)
    return redirect(reverse('accounts:login'))

@login_required
@never_cache
def profile(request):
    return render(request, 'accounts/home.html')


def profileView(request):
    user_info = {
        'first_name':request.user.first_name,
        'last_name':request.user.last_name,
        'email':request.user.email,
        'username':request.user.username,
    }
    return JsonResponse(user_info)

# class ProfileEdit(LoginRequiredMixin, UpdateView):
#     model = User
#     fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
#     template_name = 'accounts/edit.html'
#     success_url = reverse_lazy('accounts:profile')

def profileEdit(request):
    if request.user.is_authenticated:
        first_name = request.user.first_name
        last_name = request.user.last_name
        email = request.user.email
        password1 = request.user.password
        password2 = request.user.password

    return render(request, 'accounts/edit.html',{
        'first_name':first_name,
        'last_name':last_name,
        'email':email,
        'password1':password1,
        'password2':password2
    })

    


    

