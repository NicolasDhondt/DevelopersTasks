from django import forms
from django.contrib.auth import get_user_model


class ShortDeveloperForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'password']
