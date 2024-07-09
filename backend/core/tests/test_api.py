# TO RUN:
# python manage.py test core.tests.test_api

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from core.models import DatabaseUser, Equipment, Category, Catalog, Induction

class CreateUserTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('create-user')
        self.data = {
            "userID": 99999994,
            "email": "99999994@student.curtin.edu.au",
            "firstName": "John",
            "lastName": "Doe"
        }

    def tearDown(self):
        print("Tearing down the test case...")
        DatabaseUser.objects.all().delete()
        
    def test_view_users(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user_success(self):
        # Initial count of users
        initial_count = DatabaseUser.objects.count()

        # Perform POST request
        response = self.client.post(self.url, self.data, format='json')

        # Check response status
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify that a user has been added to the database and if the response is correct
        self.assertEqual(DatabaseUser.objects.count(), initial_count + 1)
        self.assertEqual(response.data['email'], self.data['email'])
        self.assertEqual(response.data['firstName'], self.data['firstName'])
        self.assertEqual(response.data['lastName'], self.data['lastName'])
        
    def test_delete_user(self):    
        create_response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        user_id = create_response.data['userID']

        delete_url = reverse('delete-user', args=[user_id]) 
        delete_response = self.client.delete(delete_url)

        # Check if the user has been deleted successfully
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify that the user is no longer in the database
        self.assertFalse(DatabaseUser.objects.filter(userID=user_id).exists())

    def test_update_user(self):
        create_response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        
        userID = create_response.data['userID']
        update_url = reverse('update-user', args=[userID])
        
        updated_data = {
            'email': self.data['email'],
            'firstName': 'Jane',
            'lastName': self.data['lastName']
        }

        update_response = self.client.put(update_url, updated_data, format='json') 
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        self.assertEqual(update_response.data['firstName'], 'Jane')

class EquipmentAPITestCase(APITestCase): 

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('create-equipment')  
        self.data = {
            "equipmentName": "Test Equipment",
            "equipmentDescription": "Description of Test Equipment"
        }

    def test_view_equipment(self):
        url = reverse('equipment-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_equipment_success(self):
        initial_count = Equipment.objects.count()
        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Equipment.objects.count(), initial_count + 1)
        self.assertEqual(response.data['equipmentName'], self.data['equipmentName'])
        self.assertEqual(response.data['equipmentDescription'], self.data['equipmentDescription'])

    def test_delete_equipment(self):
        create_response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        equipmentID = create_response.data['equipmentID']

        delete_url = reverse('delete-equipment', args=[equipmentID])  
        delete_response = self.client.delete(delete_url)

        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Equipment.objects.filter(equipmentID=equipmentID).exists())

    def test_update_equipment(self):
        create_response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        equipmentID = create_response.data['equipmentID']

        update_url = reverse('update-equipment', args=[equipmentID])  
        updated_data = self.data.copy()
        updated_data['equipmentName'] = 'Updated Equipment Name'
        update_response = self.client.put(update_url, updated_data)

        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        self.assertEqual(update_response.data['equipmentName'], 'Updated Equipment Name')
        self.assertEqual(update_response.data['equipmentDescription'], self.data['equipmentDescription'])

class CategoryAPITestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('create-category') 
        self.data = {
            "category": "TestCategory",  
            "categoryDescription": "Description of Test Category"
        }

    def test_view_category(self):
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_category_success(self):
        initial_count = Category.objects.count()

        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Category.objects.count(), initial_count + 1)
        self.assertEqual(response.data['category'], self.data['category'])
        self.assertEqual(response.data['categoryDescription'], self.data['categoryDescription'])
        
    def test_delete_category(self):
        create_response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        category = create_response.data['category']

        delete_url = reverse('delete-category', args=[category]) 
        delete_response = self.client.delete(delete_url)

        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(Category.objects.filter(category=category).exists())

    def test_update_category(self):
        create_response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        category = create_response.data['category']

        update_url = reverse('update-category', args=[category])
        updated_data = self.data.copy()
        updated_data['categoryDescription'] = 'Updated Category Description'
        update_response = self.client.put(update_url, updated_data)
        
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        
class CatalogAPITestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.category = Category.objects.create(category="TestCategory")
        self.equipment = Equipment.objects.create(equipmentName="Test Equipment", equipmentDescription="Description of Test Equipment")

        self.url = reverse('create-catalog') 
        self.data = {
            "category": self.category.category,
            "equipmentID": self.equipment.equipmentID
        }

    def test_create_catalog_success(self):
        initial_count = Catalog.objects.count()

        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Catalog.objects.count(), initial_count + 1)
        self.assertEqual(response.data['category'], self.data['category'])
        self.assertEqual(response.data['equipmentDetails']['equipmentID'], self.data['equipmentID'])

    def test_delete_catalog(self):
        catalog = Catalog.objects.create(category=self.category, equipmentID=self.equipment)

        delete_url = reverse('delete-catalog', args=[self.category.category, self.equipment.equipmentID])
        response = self.client.delete(delete_url)

        # Check the response status code (204 is standard for a successful DELETE request)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure the catalog item is deleted from the database
        self.assertFalse(Catalog.objects.filter(category=self.category, equipmentID=self.equipment).exists())

    def test_update_catalog(self):
        catalog = Catalog.objects.create(category=self.category, equipmentID=self.equipment)
        new_category = Category.objects.create(category="NewTestCategory")
        new_equipment = Equipment.objects.create(equipmentName="New Test Equipment", equipmentDescription="New Description of Test Equipment")

        update_url = reverse('update-catalog', args=[self.category.category, self.equipment.equipmentID])
        data = {
            "category": new_category.category,
            "equipmentID": new_equipment.equipmentID
        }
        response = self.client.put(update_url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_catalog = Catalog.objects.get(id=catalog.id)
        self.assertEqual(updated_catalog.category, new_category)
        self.assertEqual(updated_catalog.equipmentID, new_equipment)

        
class InductionAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = DatabaseUser.objects.create(userID="77777777")
        self.category = Category.objects.create(category="TestCategory")
        self.equipment = Equipment.objects.create(equipmentName="Test Equipment", equipmentDescription="Description of Test Equipment")

        self.url = reverse('create-induction')
        self.data = {
            "userID": self.user.userID,
            "category": self.category.category,
            "equipmentID": self.equipment.equipmentID,
            "completionStatus": "true"
        }
        
    def test_create_induction_success(self):
        initial_count = Induction.objects.count()

        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Induction.objects.count(), initial_count + 1)
        self.assertEqual(str(response.data['userDetails']['userID']), self.data['userID'])
        self.assertEqual(response.data['category'], self.data['category'])
        self.assertEqual(response.data['equipmentDetails']['equipmentID'], self.data['equipmentID'])

    def test_delete_induction(self):
        induction = Induction.objects.create(userID=self.user, category=self.category, equipmentID=self.equipment, completionStatus=True)

        delete_url = reverse('delete-induction', args=[self.user.userID, self.category.category, self.equipment.equipmentID])
        response = self.client.delete(delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Induction.objects.filter(category=self.category, equipmentID=self.equipment).exists())

    def test_update_induction(self):
        induction = Induction.objects.create(userID=self.user, category=self.category, equipmentID=self.equipment, completionStatus=True)
        new_user = DatabaseUser.objects.create(userID="44444445")
        new_category = Category.objects.create(category="NewTestCategory")
        new_equipment = Equipment.objects.create(equipmentName="New Test Equipment", equipmentDescription="New Description of Test Equipment")

        update_url = reverse('update-induction', args=[self.user.userID, self.category.category, self.equipment.equipmentID])
        data = {
            "userID": new_user.userID,
            "category": new_category.category,
            "equipmentID": new_equipment.equipmentID
        }
        response = self.client.put(update_url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_induction = Induction.objects.get(id=induction.id)
        self.assertEqual(updated_induction.category, new_category)
        self.assertEqual(updated_induction.equipmentID, new_equipment)