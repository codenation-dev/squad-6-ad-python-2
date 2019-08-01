from django.db import models
from televendas.models.comission_plan import ComissionPlan
import datetime
from televendas.models.comission_plan import ComissionPlan


class Seller(models.Model):
    """
    Model for Sellers
    """
    name = models.CharField("Nome", max_length=50, help_text="Nome completo do Vendedor")
    address = models.TextField(
        "Endereço", help_text="Endereço completo do Vendedor")
    phone_number = models.CharField(
        "Telefone", max_length=15, help_text="Número de telefone do Vendedor")
    birthday = models.DateField(
        "Data de Nascimento", help_text="Data de Nascimento do Vendedor")
    cpf = models.CharField("CPF", max_length=11, help_text="CPF do Vendedor")
    comission_plan = models.ForeignKey(
        ComissionPlan, related_name='sellers', on_delete=models.CASCADE,
        verbose_name="Plano de Comissões")
    email = models.EmailField(max_length=254, help_text="Endereço de email do Vendedor")
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
