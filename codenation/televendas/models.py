from django.db import models
import datetime

# Model Plano de Comissão
class ComissionPlan(models.Model):
    description = models.CharField("Descrição", max_length=200)
    lower_percentage = models.FloatField("Menor Porcentagem")
    min_value = models.DecimalField("Valor Mínimo", max_digits=8, decimal_places=2)
    upper_percentage = models.FloatField("Maior Porcentagem")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]
        verbose_name_plural = "Planos de Comissões"

    def __str__(self):
        return '{}'.format(self.description)

# Model Vendedor
class Seller(models.Model):
    # parece suficiente para a grande maioria dos casos
    name = models.CharField(max_length=50)
    address = models.TextField("Endereço", help_text="Address of Seller")

    # precisamos que o campo se comporte como um inteiro?
    phone_number = models.CharField(max_length=15)
    birthday = models.DateField("Data de Nascimento", help_text="Birthday of Seller")
    cpf = models.CharField(max_length=11, primary_key=True)
    comission_plan = models.ForeignKey(
                                        ComissionPlan,
                                        related_name='sellers',
                                        on_delete=models.CASCADE,
                                        verbose_name="Plano de Comissões"
                                        )

    # TODO: verificar possibilidade de validacao programatica do formato
    # deste email
    email = models.EmailField(max_length=254, help_text="Email of Seller")

    # data criacao e atualizacao
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Retorna a idade do vendedor
    @property
    def age(self):
        birthday = datetime.datetime.strptime(str(self.birthday), '%Y-%m-%d')
        today = datetime.date.today()
        return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

    def __str__(self):
        return self.name

