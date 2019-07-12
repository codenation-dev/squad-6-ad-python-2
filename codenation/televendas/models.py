from django.db import models

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
