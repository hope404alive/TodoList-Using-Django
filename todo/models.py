from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    # Relationship to the User model
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    # Title of the task
    title = models.CharField(max_length=200, null=True)
    
    # Description of the task
    description = models.TextField(null=True, blank=True)
    
    # Indicates whether the task is complete or not
    complete = models.BooleanField(default=False)
    
    # Timestamp for task creation
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
