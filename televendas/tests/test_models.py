from django.test import TestCase
from ..models import Seller
from .factories import SellerFactory

class SellerTestCase(TestCase):
    def setUp(self):
        Seller = SellerFactory()
    def test_str(self):
        """Test for string representation."""
        self.assertEqual(str(Seller), Seller.name)