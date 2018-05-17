from django.shortcuts import render, redirect

from .forms import ToDoForm
from .models import ToDoItem

# Create your views here.
def todo_view(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
    items = ToDoItem.objects.all()
    return render(request, 'todoapp/index.html', {'form':ToDoForm,'items':items,'page':'all'})

def complete(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
    items = ToDoItem.objects.filter(done=True)
    return render(request, 'todoapp/index.html', {'form':ToDoForm,'items':items,'page':'complete'})

def pending(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
    items = ToDoItem.objects.filter(done=False)
    return render(request, 'todoapp/index.html', {'form':ToDoForm,'items':items, 'page':'pending'})

def mark_done(request,item_id):
    item = ToDoItem.objects.get(id=item_id)
    item.done = True
    item.save()
    return redirect('pending')

def todo_delete(request,item_id):
    item = ToDoItem.objects.get(id=item_id)
    item.delete()
    return redirect('pending')
