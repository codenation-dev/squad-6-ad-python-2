from django.db import models


class ComissionPlan(models.Model):
    """
    Model for Comission Plan
    """
    lower_percentage = models.FloatField(
        "Menor Porcentagem", help_text="The lower comission percentage")
    min_value = models.DecimalField(
        "Valor Mínimo", max_digits=8,
        decimal_places=2,
        help_text="The minimum amount to receive bigger comission")
    upper_percentage = models.FloatField(
        "Maior Porcentagem", help_text="The bigger comission percentage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]
        verbose_name_plural = "Planos de Comissões"

    def __str__(self):
        return 'Plano {} - {}%'.format(self.min_value, self.upper_percentage)
