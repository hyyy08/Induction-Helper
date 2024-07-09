from django.urls import reverse
from core.models import DatabaseUser
from django.test import TestCase, Client

from rest_framework import status
from rest_framework.test import APITestCase

# TO RUN:
# python manage.py test core.tests.test_models

class DatabaseUserViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = DatabaseUser.objects.create(userID=99999999, email='99999999@student.curtin.edu.au', firstName='John', lastName='Doe', )
        
    def test_DatabaseUser_list_view(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.firstName)
        self.assertContains(response, self.user.lastName)
        