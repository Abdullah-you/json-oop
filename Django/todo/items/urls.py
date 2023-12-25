from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('taskedit/<int:pk>/', views.TaskEdit.as_view(), name='taskedit'),
    path('taskdetail/<int:pk>/', views.TaskDetail.as_view(), name='taskdetail'),
    path('taskcreate/', views.CreateTask.as_view(), name='taskcreate'),
]