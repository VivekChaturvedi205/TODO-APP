from django.db import models
from django.utils import timezone


class Task(models.Model):
    Task_tittle = models.CharField(max_length=100)
    Task_details = models.TextField()
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Task_tittle
