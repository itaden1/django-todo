from django.db import models

# Create your models here.

class ToDoItem(models.Model):
    todo_item = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
