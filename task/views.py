from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from .models import Task
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TaskForm
from django.shortcuts import render


class IndexTaskView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task/index.html"
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super(IndexTaskView, self).get_context_data(**kwargs)
        context['form'] = TaskForm
        return context


def create(request, devId):
    form = TaskForm(request.POST)
    if form.is_valid():
        Task.objects.create(
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            assigned=form.cleaned_data['assigned'],
        )
    if(devId == 0):
        return HttpResponseRedirect(reverse('task:index'))
    else:
        return HttpResponseRedirect(reverse('task:detail', args=[devId]))


def delete(request, taskId, devId):
    task = Task.objects.get(id=taskId)
    task.delete()
    if(devId == 0):
        return HttpResponseRedirect(reverse('task:index'))
    else:
        return HttpResponseRedirect(reverse('task:detail', args=[devId]))


def detail(request, devId):
    dev = get_user_model().objects.get(id=devId)
    tasks = Task.objects.filter(assigned=devId)
    return render(request, 'task/index.html', {'tasks': tasks,
                                               'dev': dev,
                                               'form': TaskForm})
