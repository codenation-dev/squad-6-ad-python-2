import factory
from faker import Faker
from ..models import ComissionPlan, Seller, Sale
import random

fake = Faker('pt_BR')

def generate_cpf():                                                        
    cpf = [random.randint(0, 9) for x in range(9)]                                                                                                              
    for _ in range(2):                                                          
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11                                                                                      
        cpf.append(11 - val if val > 1 else 0)                                                                                                                  
    return '%s%s%s%s%s%s%s%s%s%s%s' % tuple(cpf)

class ComissionPlanFactory(factory.DjangoModelFactory):
    lower_percentage = fake.pyfloat(left_digits=3, right_digits=2, positive=True, min_value=0, max_value=5)
    min_value = fake.pydecimal(left_digits=None, right_digits=2, positive=True, min_value=1000, max_value=10000)
    upper_percentage = fake.pyfloat(left_digits=3, right_digits=2, positive=True, min_value=0, max_value=10)
    class Meta:
        model = ComissionPlan

class SellerFactory(factory.DjangoModelFactory):
    name = fake.name()
    address = fake.address()
    phone = fake.msisdn()
    age = fake.pyint(min=18, max=65, step=1)
    email = fake.email()
    cpf = generate_cpf()
    comission_plan = factory.SubFactory(ComissionPlanFactory)
    class Meta:
        model = Seller

class SaleFactory(factory.DjangoModelFactory):
    seller = factory.SubFactory(SellerFactory)
    month = fake.pyint(min=1, max=12, step=1)
    amount = fake.pydecimal(left_digits=None, right_digits=2, positive=True, min_value=1000, max_value=10000)
    class Meta:
        model = Sale