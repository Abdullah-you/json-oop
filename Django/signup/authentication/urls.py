from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('home/', views.home, name='home'),
    path('forget_password/', views.forget_password, name='forget-password'),
    #path('forget-password/', views.forget_password, name='forget-password'),
   # path('change-password', views.change_password, name='change-password'),
]