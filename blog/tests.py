from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post

class BlogTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser('homer', 'a@a.ru', 'simpson')
        self.post = Post.objects.create(title='Hi', author=self.user, text='text')

    def test_create(self):
        response = self.client.post(reverse('create'), {'title': 'test', 'author': self.user, 'text': 'try'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test')
        self.assertTemplateUsed(response, 'create.html')

    def test_read(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_update(self):
        response = self.client.post(reverse('edit', args=['1']), {'title': 'update', 'text': 'updated text'})
        self.assertEqual(response.status_code, 302)

    def test_delete(self):
        response = self.client.get(reverse('delete', args=['1']))
        self.assertEqual(response.status_code, 200)