import datetime
from django.test import TestCase
from televendas.models.comission_plan import ComissionPlan
from .factories import ComissionPlanFactory


class ComissionPlanTestCase(TestCase):
    """This class defines the test suite for the ComissionPlan model."""
    def test_model_can_create_a_comission_plan(self):
        """Test the ComissionPlan model can create a ComissionPlan."""
        old_count = ComissionPlan.objects.count()
        self.comission_plan = ComissionPlanFactory()
        new_count = ComissionPlan.objects.count()
        self.assertNotEqual(old_count, new_count)
