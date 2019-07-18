from django.db import models

# Create your models here.

class Seller(models.Model):
    # parece suficiente para a grande maioria dos casos
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)

    # precisamos que o campo se comporte como um inteiro?
    phone_number = models.CharField(max_length=15)
    age = models.CharField(max_length=3)
    cpf = models.CharField(max_length=11, primary_key=True)
    comission_plan = models.CharField(max_length=2)

    # TODO: verificar possibilidade de validacao programatica do formato
    # deste email
    email = models.CharField(max_length=50)
