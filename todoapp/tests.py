from django.test import TestCase

from .views import todo_view
from .forms import ToDoForm
from .models import ToDoItem
# Create your tests here.
class ToDoPageTest(TestCase):
    '''Test the to do app page'''

    def test_root_url_returns_correct_page(self):
        response = self.client.get('/')
        content = response.content.decode('utf-8')
        self.assertIn('To Do List', content)

    def test_todo_form_validates(self):
        form = ToDoForm(data={'todo_item':'hang out washing'})
        self.assertTrue(form.is_valid(), form.errors)

    def test_todo_form_saves_data(self):
        self.client.post('/',data={'todo_item':'hang out washing'})
        response = self.client.get('/')
        content = response.content.decode('utf-8')
        self.assertIn('hang out washing', content)

    def test_can_delete_item(self):
        self.client.post('/',data={'todo_item':'hang out washing'})
        response = self.client.get('/delete/1', follow=True)
        self.assertRedirects(response, '/')
        #response = self.client.get('/')
        content = response.content.decode('utf-8')
        self.assertNotIn('hang out washing', content)
        
