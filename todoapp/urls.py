from django.urls import path

from .views import todo_view, todo_delete, pending, complete, mark_done

urlpatterns = [
        path('', todo_view, name='todo'),
        path('mark-done/<int:item_id>', mark_done, name='mark done'),
        path('pending', pending, name='pending'),
        path('complete', complete, name='complete'),
        path('delete/<int:item_id>', todo_delete, name='todo delete'),
        ]
