from django.urls import reverse
from core.models import DatabaseUser
from django.test import TestCase, Client

from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

class DatabaseUserViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = DatabaseUser.objects.create(userID=40984098, firstName='John', lastName='Doe', )
        
    def test_DatabaseUser_list_view(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.firstName)
        self.assertContains(response, self.user.lastName)
        

    def test_user_login(self):
        url = reverse('user-login')

        # Data to be sent in the request
        data = {'username': 'admin', 'password': '2030'}

        # Send POST request
        response = self.client.post(url, data, format='json')

        # Check that the response status
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check the content of the response (assuming the response contains a 'message' key)
        self.assertEqual(response.data['message'], 'Login successful')


class DatabaseUserAPITestCase(APITestCase):
    def setUpAPI(self):
        # Create a test user in the database
        DatabaseUser.objects.create(
            userID=19041893,
            tutorID=None, 
            email="test@example.com",
            firstName="Test",
            lastName="User",
            userDate=timezone.now().date(),  
            userLevel="student",
        )
        
    def test_get_users(self):
        """
        Ensure we can retrieve the list of users.
        """
        # Get the response by making a GET request to the API endpoint
        url = reverse('user-list')
        response = self.client.get(url)
        
        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Assuming your serializer returns all fields, check if the response data is as expected
        # Modify this according to your actual serializer output
        expected_response_data = [{
            "userID": 1,
            "tutorID": None,
            "email": "test@example.com",
            "firstName": "Test",
            "lastName": "User",
            "userDate": timezone.now().date().isoformat(),  # Matching the format of the response
        }]
        
        self.assertEqual(response.data, expected_response_data)
