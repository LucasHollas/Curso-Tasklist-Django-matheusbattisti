from django.urls import path

from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('yourname/<str:name>', views.yourName, name="your-name")
]