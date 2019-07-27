
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('televendas', '0003_auto_20190724_2024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField(
                    help_text='Address of Seller', verbose_name='Endereço')),
                ('phone_number', models.CharField(max_length=15)),
                ('birthday', models.DateField(
                    help_text='Birthday of Seller',
                    verbose_name='Data de Nascimento')),
                ('cpf', models.CharField(
                    max_length=11, primary_key=True, serialize=False)),
                ('email', models.EmailField(
                    help_text='Email of Seller', max_length=254)),
                ('created_at', models.DateTimeField(
                    auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comission_plan', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='sellers', to='televendas.ComissionPlan',
                    verbose_name='Plano de Comissões')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(
                    decimal_places=2, max_digits=8)),
                ('month', models.CharField(
                    choices=[
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
                        ('12', 'dezembro')
                    ], max_length=1)),
                ('comission', models.DecimalField(
                    decimal_places=2, max_digits=8)),
                ('seller', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='televendas.Seller', verbose_name='CPF')),
            ],
            options={
                'db_table': 'sale',
            },
        ),
    ]
