import factory
from faker import Faker
from televendas.models.comission_plan import ComissionPlan

fake = Faker('pt_BR')

class ComissionPlanFactory(factory.DjangoModelFactory):
    lower_percentage = fake.pyfloat(left_digits=3, right_digits=2, positive=True, min_value=0, max_value=5)
    min_value = fake.pydecimal(left_digits=None, right_digits=2, positive=True, min_value=1000, max_value=10000)
    upper_percentage = fake.pyfloat(left_digits=3, right_digits=2, positive=True, min_value=0, max_value=10)
    class Meta:
        model = ComissionPlan