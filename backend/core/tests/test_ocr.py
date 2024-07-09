from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
import os

class OCRViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_ocr_view_no_image(self):
        response = self.client.post('/ocr/', {}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'No image provided')

    def test_ocr_view_with_sample_image(self):
        # Load the sample image
        sample_image_path = os.path.join(os.path.dirname(__file__), 'resources', 'TestPhoto.jpg')
        with open(sample_image_path, 'rb') as image_file:
            image_data = image_file.read()

        image_file = SimpleUploadedFile("TestPhoto.jpg", image_data, content_type="image/jpeg")

        response = self.client.post('/ocr/', {'image': image_file}, format='multipart')

        print("Response Data:", response.data)  # Debug print to check response data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['firstName'], 'John')  # Update firstName
        self.assertEqual(response.data['lastName'], 'SMITH')    # Update lastName
        self.assertEqual(response.data['studentNumber'], '99999999')  # studentNumber
