from django.test import TestCase
from ..models import Seller, ComissionPlan
from .factories import SellerFactory, ComissionPlanFactory

class SellerTestCase(TestCase):
    """This class defines the test suite for the seller model."""
    def test_model_can_create_a_seller(self):
        """Test the seller model can create a seller."""
        old_count = Seller.objects.count()
        self.seller = SellerFactory()
        new_count = Seller.objects.count()
        self.assertNotEqual(old_count, new_count)


class ComissionPlanTestCase(TestCase):
    """This class defines the test suite for the ComissionPlan model."""
    def test_model_can_create_a_comission_plan(self):
        """Test the ComissionPlan model can create a ComissionPlan."""
        old_count = ComissionPlan.objects.count()
        self.comission_plan = ComissionPlanFactory()
        new_count = ComissionPlan.objects.count()
        self.assertNotEqual(old_count, new_count)