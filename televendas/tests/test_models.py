from django.test import TestCase
from ..models import Seller, ComissionPlan, Sale
from .factories import SellerFactory, ComissionPlanFactory, SaleFactory

class ComissionPlanTestCase(TestCase):
    """This class defines the test suite for the ComissionPlan model."""
    def test_model_can_create_a_comission_plan(self):
        """Test the ComissionPlan model can create a ComissionPlan."""
        old_count = ComissionPlan.objects.count()
        self.comission_plan = ComissionPlanFactory()
        new_count = ComissionPlan.objects.count()
        self.assertNotEqual(old_count, new_count)

class SellerTestCase(TestCase):
    """This class defines the test suite for the seller model."""
    def test_model_can_create_a_seller(self):
        """Test the seller model can create a seller."""
        old_count = Seller.objects.count()
        self.seller = SellerFactory()
        new_count = Seller.objects.count()
        self.assertNotEqual(old_count, new_count)

class SaleTestCase(TestCase):
    """This class defines the test suite for the Sale model."""
    def test_model_can_create_a_sale(self):
        """Test the Sale model can create a Sale."""
        old_count = Sale.objects.count()
        self.sale = SaleFactory()
        new_count = Sale.objects.count()
        self.assertNotEqual(old_count, new_count)