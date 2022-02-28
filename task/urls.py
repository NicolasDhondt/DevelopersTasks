from django.urls import path
from .views import IndexTaskView
from . import views

app_name = 'task'

urlpatterns = [
    path('', IndexTaskView.as_view(), name='index'),
    path('create/<int:devId>', views.create, name='create'),
    path('delete/<int:taskId>/<int:devId>', views.delete, name='delete'),
    path('detail/<int:devId>', views.detail, name='detail'),
]
