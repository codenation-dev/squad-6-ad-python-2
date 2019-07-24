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

#Modelo de registro de Vendas
class Sale(models.Model):
    
    class Meta:
        db_table = 'sale'

        
    months=(
        ('1', 'janeiro'),
        ('2', 'fevereiro'),
        ('3', 'março'),
        ('4', 'abril'),
        ('5', 'maio'),
        ('6', 'junho'),
        ('7', 'julho'),
        ('8', 'agosto'),
        ('9', 'setembro'),
        ('10', 'outubro'),
        ('11', 'novembro'),
        ('12', 'dezembro'),
    )


    seller = models.ForeignKey(Seller , on_delete=models.CASCADE, verbose_name="CPF") 
    amount =  models.DecimalField(max_digits=8, decimal_places=2) #aqui fui deacordo com o modelo ComissionPlan com o número de digitos, e exibição dos decimais
    month = models.CharField( choices=months , max_length=1)
    comission = models.DecimalField( max_digits=8, decimal_places=2) 

