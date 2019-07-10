from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import ComissionPlan, Seller
from .factories import ComissionPlanFactory

class ComissionPlanViewTestCase(APITestCase):
    def test_create_ComissionPlan(self):
        """
        Ensure we can create a new ComissionPlan object.
        """
        url = reverse('comissionplan-list')
        comission_plan_data = {
                "lower_percentage": 2,
                "min_value": 3000.0,
                "upper_percentage": 5,
        }
        response = self.client.post(url, comission_plan_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ComissionPlan.objects.count(), 1)
        self.assertEqual(ComissionPlan.objects.get().min_value, 3000.0)

class SellerViewTestCase(APITestCase):
    def test_create_seller(self):
        """
        Ensure we can create a new seller object.
        """
        url = reverse('seller-list')
        #create a comission plan id 1
        comission_plan = ComissionPlanFactory()
        seller_data = {
            'name': 'John Doe', 
            'address': 'Rua dos Maristas, 7, 7', 
            'phone': 7192680548, 
            'age': 29, 
            'email': 'johndoe@gmail.com',
            'cpf': 1241241241,
            'comission_plan': 1
        }
        response = self.client.post(url, seller_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Seller.objects.count(), 1)
        self.assertEqual(Seller.objects.get().name, 'John Doe')