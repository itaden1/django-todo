from django.forms import ModelForm, CharField
from .models import ToDoItem

class ToDoForm(ModelForm):
    todo_item = CharField(label='New todo item', max_length=200)

    class Meta:
        model = ToDoItem
        fields = ['todo_item']
