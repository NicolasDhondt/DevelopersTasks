from django.shortcuts import render
from django.views.generic import ListView

from developer.models import Developer

# Create your views here.


class IndexView(ListView):
    model = Developer
    template_name = "developer/index.html"
    context_object_name = 'developers'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context
