from django.db import models
import datetime
from django.core.mail import send_mail

# Model Plano de Comissão
class PlanoComissoes(models.Model):
    descricao = models.CharField("Descrição", max_length=200)
    porcentagem_menor = models.PositiveIntegerField()
    valor_minimo = models.DecimalField(max_digits=8, decimal_places=2)
    porcentagem_maior = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]
        verbose_name_plural = "Planos de Comissões"

    def __str__(self):
        return self.descricao

# Model para Vendedor    
class Vendedor(models.Model):
    nome = models.CharField("Nome", max_length=200)
    cep = models.IntegerField()
    logradouro = models.CharField("Logradouro", max_length=200)
    numero_casa = models.CharField("Número da Casa", max_length=50)
    bairro = models.CharField("Bairro", max_length=50)
    cidade = models.CharField("Cidade", max_length=50)
    estado = models.CharField("UF",max_length=2)
    telefone = models.CharField("Telefone", max_length=50)
    data_nascimento = models.DateField("Data de Nascimento")
    email = models.EmailField(max_length=254)
    cpf = models.CharField("CPF", max_length=11)
    plano_de_comissao = models.ForeignKey(PlanoComissoes, related_name='vendedores', on_delete=models.CASCADE, verbose_name="Plano de Comissãos")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def idade(self):
        "Retorna a idade do vendedor."
        self.data_nascimento
        today = datetime.date.today()
        return today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))
    
    @property
    def maior_comissao(self):
        "retorna maior comissao."
        try:
            venda = Venda.objects.filter(vendedor_id=self.id).order_by('-valor_comissao').first() 
            return venda.valor_comissao
        except Exception as e:
            pass

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["created_at"]
        verbose_name_plural = "Vendedores"

# Model para Vendas
class Venda(models.Model):
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
    vendedor = models.ForeignKey(Vendedor, related_name='vendas', on_delete=models.CASCADE)
    mes = models.CharField("Mês", choices=MESES, max_length=2)
    ano = models.CharField("Ano", max_length=4)
    valor_vendas = models.DecimalField("Valor das Vendas", max_digits=8, decimal_places=2)
    valor_comissao = models.DecimalField("Valor da Comissão", max_digits=8, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    #Salva o valor da Comissão
    def save(self, *args, **kwargs):
        #Calculando Comissao
        plano_comissao = self.vendedor.plano_de_comissao
        if self.valor_vendas < plano_comissao.valor_minimo:
            self.valor_comissao = (plano_comissao.porcentagem_menor/100)*float(self.valor_vendas)
        self.valor_comissao = (plano_comissao.porcentagem_maior/100)*float(self.valor_vendas)
        super(Venda, self).save(*args, **kwargs)
        
    class Meta:
        ordering = ["created_at"]
        verbose_name_plural = "Vendas"
        unique_together = ("vendedor", "mes", "ano")  

    def __str__(self):
       return 'Vendas {}/{}'.format(self.mes, self.ano)
