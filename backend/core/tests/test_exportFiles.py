import tempfile
from django.test import TestCase, Client
from django.urls import reverse
from core.models import DatabaseUser, Induction, Equipment, Category
from core.views import exportFiles_views
import csv



class ExportFilesTestCase(TestCase):
    def setUp(self):
        # Create a temporary directory for storing test files
        self.temp_dir = tempfile.TemporaryDirectory()

        # Create some test data
        self.database_user = DatabaseUser.objects.create(userID=1, email='test@example.com', firstName='John', lastName='Doe')
    
        # Create an Equipment instance
        self.equipment = Equipment.objects.create(barcode='123456', equipmentName='Test Equipment', equipmentDescription='Description')
    
        # Create a Category instance
        self.category = Category.objects.create(category='Test', categoryDescription='Test Description')

        # Create an Induction object with the Equipment and Category instances
        self.induction = Induction.objects.create(userID=self.database_user, barcode=self.equipment, category=self.category, completionStatus=True)


    def test_export_to_pdf(self):
        # Test exporting data users to PDF
        client = Client()
        response = client.get(reverse('export_user_pdf'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')

    def test_export_to_csv(self):
        # Test exporting data users to CSV
        client = Client()
        response = client.get(reverse('export_user_csv'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/csv')

    def test_export_induction_to_pdf(self):
        # Test exporting all users' induction data to PDF
        client = Client()
        response = client.get(reverse('export_induction_to_pdf'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')

    def test_export_induction_to_csv(self):
        # Test exporting all users' induction data to CSV
        client = Client()
        response = client.get(reverse('export_induction_to_csv'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/csv')
