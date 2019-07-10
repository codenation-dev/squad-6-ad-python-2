from django.test import TestCase
from ..serializers import SellerSerializer
from .factories import SellerFactory


class SellerSerializerTestCase(TestCase):
    def test_model_fields(self):
        """Serializer data matches the Seller object for each field."""
        seller = SellerFactory()
        serializer = SellerSerializer(seller)
        for field_name in [
            'id', 'name', 'address', 'phone', 'age', 'email', 'cpf', 
            'comission_plan', 'created_at', 'updated_at'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(seller, field_name)
            )