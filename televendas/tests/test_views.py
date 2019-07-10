from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from ..models import ComissionPlan, Seller
from .factories import SellerFactory

class SellerViewSetTestCase(TestCase):
      def setUp(self):
          self.list_url = reverse('seller-list')

      def get_detail_url(self, seller_id):
          return reverse(self.seller-detail, kwargs={'id': seller_id})

      def test_get_list(self):
          """GET the list page of Sellers."""
          sellers = [SellerFactory() for i in range(0, 3)]

          response = self.client.get(self.list_url)

          self.assertEqual(response.status_code, status.HTTP_200_OK)
          self.assertEqual(
              set(seller['id'] for seller in response.data['results']),
              set(seller.id for seller in sellers)
          )

      def test_get_detail(self):
          """GET a detail page for a seller."""
          seller = SellerFactory()
          response = self.client.get(self.get_detail_url(seller.id))
          self.assertEqual(response.status_code, status.HTTP_200_OK)
          self.assertEqual(response.data['name'], seller.name)

      def test_post(self):
          """POST to create a Seller."""
          data = {
                "name": "John Doe",
                "address": "Rua dos Maristas, 7, 7",
                "phone": "7192680548",
                "idade": 29,
                "email": "johndoe@gmail.com",
                "cpf": "08863187153",
                "comission_plan": "1",
          }
          self.assertEqual(Seller.objects.count(), 0)
          response = self.client.post(self.list_url, data=data)
          self.assertEqual(response.status_code, status.HTTP_201_CREATED)
          self.assertEqual(Seller.objects.count(), 1)
          seller = Seller.objects.all().first()
          for field_name in data.keys():
                self.assertEqual(getattr(seller, field_name), data[field_name])

      def test_put(self):
          """PUT to update a seller."""
          seller = SellerFactory()
          data = {
               "name": "John Doe updated",
                "address": "Rua dos Maristas, 7, 7",
                "phone": "7192680548",
                "idade": 29,
                "email": "johndoe@gmail.com",
                "cpf": "08863187153",
                "comission_plan": "1",
          }
          response = self.client.put(
              self.get_detail_url(seller.id),
              data=data
          )
          self.assertEqual(response.status_code, status.HTTP_200_OK)

          # The object has really been updated
          seller.refresh_from_db()
          for field_name in data.keys():
              self.assertEqual(getattr(seller, field_name), data[field_name])

      def test_patch(self):
          """PATCH to update a Seller."""
          seller = SellerFactory()
          data = {'name': 'New name'}
          response = self.client.patch(
              self.get_detail_url(seller.id),
              data=data
          )
          self.assertEqual(response.status_code, status.HTTP_200_OK)

          # The object has really been updated
          seller.refresh_from_db()
          self.assertEqual(seller.name, data['name'])

      def test_delete(self):
          """DELETEing is not implemented."""
          seller = SellerFactory()
          response = self.client.delete(self.get_detail_url(seller.id))
          self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)