from django.db import models
from django.contrib.auth import get_user_model


class Task(models.Model):
    title = models.CharField('title', max_length=30, unique=True)
    description = models.TextField('description', max_length=500)
    assigned = models.ForeignKey(get_user_model(), related_name="tasks",
                                 on_delete=models.CASCADE, blank=True, null=True, verbose_name="assigned")
    dateTimeCreation = models.DateTimeField('date', auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.description})"
