from django.db import models

# Create your models here.


class Todo(models.Model):
    Priority = ((1, 'high'), (2, 'medium'), (3, 'low'))
    task = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    priority = models.SmallIntegerField(choices=Priority, default=3)
    is_done = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task
