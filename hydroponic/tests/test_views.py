from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from hydroponic.models import HydroponicSystem, Measurement

class HydroponicSystemTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.hydroponic_system = HydroponicSystem.objects.create(name='Test System', description='Test Description', owner=self.user)
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_hydroponic_system(self):
        url = '/api/hydroponic_system/'
        data = {'name': 'New System', 'description': 'New Description', 'owner': self.user.id}
        response = self.client.post(url, data, format='json')
        print(response.data)  # Print the response data for debugging
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(HydroponicSystem.objects.count(), 2)
        self.assertEqual(HydroponicSystem.objects.get(id=2).name, 'New System')

    def test_get_hydroponic_system(self):
        url = f'/api/hydroponic_system/{self.hydroponic_system.id}/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test System')

    def test_update_hydroponic_system(self):
        url = f'/api/hydroponic_system/{self.hydroponic_system.id}/'
        data = {'name': 'Updated System', 'description': 'Updated Description', 'owner': self.user.id}
        response = self.client.put(url, data, format='json')
        print(response.data)  # Print the response data for debugging
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.hydroponic_system.refresh_from_db()
        self.assertEqual(self.hydroponic_system.name, 'Updated System')

    def test_delete_hydroponic_system(self):
        url = f'/api/hydroponic_system/{self.hydroponic_system.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(HydroponicSystem.objects.count(), 0)

class MeasurementTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.hydroponic_system = HydroponicSystem.objects.create(name='Test System', description='Test Description', owner=self.user)
        self.measurement = Measurement.objects.create(hydroponic_system=self.hydroponic_system, ph=6.5, temperature=22.0, tds=300)
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_measurement(self):
        url = '/api/measurement/'
        data = {'hydroponic_system': self.hydroponic_system.id, 'ph': 7.0, 'temperature': 23.0, 'tds': 320}
        response = self.client.post(url, data, format='json')
        print(response.data)  # Print the response data for debugging
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Measurement.objects.count(), 2)
        self.assertEqual(Measurement.objects.get(id=2).ph, 7.0)

    def test_get_measurement(self):
        url = f'/api/measurement/{self.measurement.id}/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['ph'], 6.5)

    def test_update_measurement(self):
        url = f'/api/measurement/{self.measurement.id}/'
        data = {'ph': 6.8, 'temperature': 23.0, 'tds': 310, 'hydroponic_system': self.hydroponic_system.id}
        response = self.client.put(url, data, format='json')
        print(response.data)  # Print the response data for debugging
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.measurement.refresh_from_db()
        self.assertEqual(self.measurement.ph, 6.8)

    def test_delete_measurement(self):
        url = f'/api/measurement/{self.measurement.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Measurement.objects.count(), 0)
