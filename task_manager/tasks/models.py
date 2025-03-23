from django.db import models
from django.contrib.auth.models import User


# Create your models here


class Task(models.Model):
    
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    priority_level = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.BooleanField(default=False)  # False = Pending while True = Completed
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title

