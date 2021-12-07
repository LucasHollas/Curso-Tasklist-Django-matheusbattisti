from django.urls import path

from . import views

urlpatterns = [
    path('', views.taskList, name='list'),
    path('task/<int:id>', views.taskView, name="task-view"),
    path('newtask/', views.newTask, name="new-task"),
    path('edit/<int:id>', views.editTask, name="edit-task"),
    path('changeStatus/<int:id>', views.changeStatus, name="change-status"),
    path('delete/<int:id>', views.deleteTask, name="delete-task"), 
    path('yourname/<str:name>', views.yourName, name="your-name")
]