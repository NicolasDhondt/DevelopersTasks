from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from developer.forms import ShortDeveloperForm


# Create your views here.


class IndexDevView(ListView):
    model = get_user_model()
    template_name = "developer/index.html"
    context_object_name = 'developers'

    def get_context_data(self, **kwargs):
        context = super(IndexDevView, self).get_context_data(**kwargs)
        context['form'] = ShortDeveloperForm
        return context


def create(request):
    form = ShortDeveloperForm(request.POST)
    if form.is_valid():
        get_user_model().objects.create_user(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )
    return HttpResponseRedirect(reverse('developer:index'))


def delete(request, devId):
    if request.user.is_authenticated:
        dev = get_user_model().objects.get(id=devId)
        dev.delete()
        return HttpResponseRedirect(reverse('developer:index'))
    else:
        return HttpResponseRedirect(reverse('login'))
