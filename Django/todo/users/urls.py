from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('home/', views.Home.as_view(), name='home'),
    path('logout/', views.logoutView, name='logout'),
]