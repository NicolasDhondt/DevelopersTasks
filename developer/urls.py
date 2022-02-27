from django.urls import path

from .views import IndexDevView
from developer import views


app_name = 'developer'

urlpatterns = [
    path('', IndexDevView.as_view(), name='index'),
    path('create', views.create, name='create'),
    path('delete/<int:devId>', views.delete, name='delete'),
]
