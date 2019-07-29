from django.db import models
from televendas.models.comission_plan import ComissionPlan
import datetime


class Seller(models.Model):
    """
    Model for Sellers
    """
    name = models.CharField(max_length=50)
    address = models.TextField("Endereço", help_text="Address of Seller")
    phone_number = models.CharField(max_length=15)
    birthday = models.DateField(
        "Data de Nascimento", help_text="Birthday of Seller")
    cpf = models.CharField(max_length=11, primary_key=True)
    comission_plan = models.ForeignKey(
        ComissionPlan, related_name='sellers', on_delete=models.CASCADE,
        verbose_name="Plano de Comissões")
    email = models.EmailField(max_length=254, help_text="Email of Seller")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def age(self):
        birthday = datetime.datetime.strptime(str(self.birthday), '%Y-%m-%d')
        today = datetime.date.today()
        return today.year - birthday.year - ((today.month, today.day) <
                                             (birthday.month, birthday.day))

    def __str__(self):
        return self.name
