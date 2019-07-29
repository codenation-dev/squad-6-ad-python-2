from django.db import models
from televendas.models.seller import Seller


class Sale(models.Model):
    """
    Model for Sales
    """
    months = (
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
    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE, verbose_name="CPF")
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    month = models.CharField(choices=months, max_length=1)
    comission = models.DecimalField(
        max_digits=8, decimal_places=2, editable=False)

    @property
    def get_comission(self):
        comission_plan = self.seller.comission_plan
        if self.amount < comission_plan.min_value:
            comission =\
                (comission_plan.lower_percentage/100)*float(self.amount)
        else:
            comission =\
                (comission_plan.upper_percentage/100)*float(self.amount)
        return comission

    def save(self, *args, **kwargs):
        self.comission = self.get_comission

    class Meta:
        db_table = 'sale'
