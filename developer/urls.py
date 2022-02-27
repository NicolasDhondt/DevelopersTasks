from django.urls import path
from .views import IndexView
from developer import views


app_name = 'developer'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create', views.create, name='create'),
    path('delete/<int:devId>', views.delete, name='delete'),
]
