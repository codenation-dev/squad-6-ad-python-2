from django.db import models
import datetime
from django.core.mail import send_mail

# Model Plano de Comissão
class ComissionPlan(models.Model):
    lower_percentage = models.FloatField("Menor Porcentagem")
    min_value = models.DecimalField("Valor Mínimo", max_digits=8, decimal_places=2)
    upper_percentage = models.FloatField("Maior Porcentagem")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]
        verbose_name_plural = "Planos de Comissões"

    def __str__(self):
        return 'Plano {} - {}%'.format(self.min_value, self.upper_percentage)


# Model para Seller    
class Seller(models.Model):
    name = models.CharField("Name", max_length=200)
    address = models.TextField("Endereço")
    phone = models.PositiveIntegerField("Telefone")
    age = models.PositiveIntegerField("Idade")
    email = models.EmailField(max_length=254)
    cpf = models.PositiveIntegerField("CPF")
    comission_plan = models.ForeignKey(ComissionPlan, related_name='sellers', on_delete=models.CASCADE, verbose_name="Plano de Comissãos")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created_at"]
        verbose_name_plural = "Selleres"

# Model para Vendas
class Sale(models.Model):
    MESES = (
        ('1', 'Janeiro'),
        ('2', 'Fevereiro'),
        ('3', 'Março'),
        ('4', 'Abril'),
        ('5', 'Maio'),
        ('6', 'Junho'),
        ('7', 'Julho'),
        ('8', 'Agosto'),
        ('9', 'Setembro'),
        ('10', 'Outubro'),
        ('11', 'Novembro'),
        ('12', 'Dezembro'),
    )
    seller = models.ForeignKey(Seller, related_name='sales', on_delete=models.CASCADE)
    month = models.CharField("Mês", choices=MESES, max_length=2)
    amount = models.DecimalField("Valor das Vendas", max_digits=8, decimal_places=2)
    comission = models.DecimalField("Valor da Comissão", max_digits=8, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    #Salva o valor da Comissão
    def save(self, *args, **kwargs):
        #Calculando Comissao
        comission_plan = self.seller.comission_plan
        if self.amount < comission_plan.min_value:
            self.comission = (comission_plan.lower_percentage/100)*float(self.amount)
        self.comission = (comission_plan.upper_percentage/100)*float(self.amount)
        super(Sale, self).save(*args, **kwargs)
        
    class Meta:
        ordering = ["created_at"]
        verbose_name_plural = "Vendas"
        unique_together = ("seller", "month")  

    def __str__(self):
       return 'Vendas {}/{}'.format(self.mes, self.ano)
