from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Developer(AbstractUser):
    first_name = models.CharField("first name", max_length=20)
    last_name = models.CharField("last name", max_length=20)

    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
