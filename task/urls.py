from django.urls import path
from .views import IndexView
from . import views

app_name = 'task'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create', views.create, name='create'),
    path('delete/<int:taskId>', views.delete, name='delete'),
]
