#test_userupload.py
#unittest for user csv upload and process feature
#to run, use: python manage.py test core.tests.test_userupload"
from django.urls import reverse
from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
import io, os

class CSVImportTestCase(TestCase):
    def setUp(self):
        # Set up data if necessary
        self.client = Client()
        self.url = reverse('user-upload')  # Assume 'user-upload' is the name of the URL for the upload view

    def test_valid_csv_upload(self):
        # Create CSV file with correct data
        csv_data = b'barcode,email,firstname,surname\n123456,james@student.curtin.edu.au,James,Ng'
        csv_file = SimpleUploadedFile("test.csv", csv_data, content_type='text/csv')

        # Post
        response = self.client.post(self.url, {'file': csv_file}, follow=True)

        # Pass if response is HTTP_201_CREATED
        self.assertEqual(response.status_code, 201)
        
    def test_partial_csv_upload(self):
        # Create CSV file that has both invalid and valid data
        csv_data = (
            b'barcode,email,firstname,surname\n'
            b'123456,james@student.curtin.edu.au,James,Ng\n'#CORRECT ROW
            b'a12345a,jon@student.curtin.edu.au,Jon,Sur\n'#barcode contain non-integer
            b'232424,bob@student.curtin.edu.au,,Cobb\n'#missing firstname field
            b'1234500,ben.nguyen@student.curtin.edu.au,Ben,Nguyen\n'#CORRECT ROW
            b'000001,bam@student.curtin.edu.au,Bam,\n'#missing surname field
            
        )
        csv_file = SimpleUploadedFile("test.csv", csv_data, content_type='text/csv')

        # Post
        response = self.client.post(self.url, {'file': csv_file}, follow=True)

        # Pass if response is HTTP_207_MULTI_STATUS
        self.assertEqual(response.status_code, 207)
        self.assertIn("Processed 2 records successfully.", response.content.decode())

    def test_invalid_csv_upload(self):
        # Create CSV file with invalid data missing fields
        csv_data = b'barcode,email,firstname,surname\n,invalidemail@,James,Ng'
        csv_file = SimpleUploadedFile("invalid_test.csv", csv_data, content_type='text/csv')

        # Post
        response = self.client.post(self.url, {'file': csv_file}, follow=True)

        # Test pass if response is 400 BAD REQUEST
        self.assertEqual(response.status_code, 400)

    def test_empty_csv_upload(self):
        # Test uploading an empty CSV
        csv_data = b''
        csv_file = SimpleUploadedFile("empty.csv", csv_data, content_type='text/csv')

        # Post
        response = self.client.post(self.url, {'file': csv_file}, follow=True)

        # Test pass if response is 400 BAD REQUEST
        self.assertEqual(response.status_code, 400)

    def test_large_csv_upload(self):
        # Use large CSV file
        file_path = os.path.join(os.path.dirname(__file__), 'large_test_data.csv')
        with open(file_path, 'rb') as f:
            csv_file = SimpleUploadedFile("large_test_data.csv", f.read(), content_type='text/csv')
        # Post
        response = self.client.post(self.url, {'file': csv_file}, follow=True)
        # Test pass if response is HTTP 201_CREATED
        self.assertEqual(response.status_code, 201)