from django.test import TestCase
from django.urls import reverse
from .models import Todo

class TodoModelTest(TestCase):
    def test_create_todo(self):
        todo = Todo.objects.create(title='Test', description='Desc')
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(todo.title, 'Test')

class TodoViewTest(TestCase):
    def test_todo_list_view(self):
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/home.html')

    def test_create_todo_view(self):
        response = self.client.post(reverse('todo_create'), {
            'title': 'New Task',
            'description': 'Description',
            'resolved': False
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todo.objects.count(), 1)
