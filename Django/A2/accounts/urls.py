from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserCreate.as_view(), name='signup'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('profile/view/', views.profileView, name='view'),
    path('logout/', views.LogoutView, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('profile/edit/', views.profileEdit, name='edit'),
]