# Generated by Django 2.2.3 on 2019-07-31 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComissionPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lower_percentage', models.FloatField(help_text='The lower comission percentage', verbose_name='Menor Porcentagem')),
                ('min_value', models.DecimalField(decimal_places=2, help_text='The minimum amount to receive bigger comission', max_digits=8, verbose_name='Valor Mínimo')),
                ('upper_percentage', models.FloatField(help_text='The bigger comission percentage', verbose_name='Maior Porcentagem')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Planos de Comissões',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nome completo do Vendedor', max_length=50, verbose_name='Nome')),
                ('address', models.TextField(help_text='Endereço completo do Vendedor', verbose_name='Endereço')),
                ('phone_number', models.CharField(help_text='Número de telefone do Vendedor', max_length=15, verbose_name='Telefone')),
                ('birthday', models.DateField(help_text='Data de Nascimento do Vendedor', verbose_name='Data de Nascimento')),
                ('cpf', models.CharField(help_text='CPF do Vendedor', max_length=11, verbose_name='CPF')),
                ('email', models.EmailField(help_text='Endereço de email do Vendedor', max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comission_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sellers', to='televendas.ComissionPlan', verbose_name='Plano de Comissões')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('month', models.CharField(choices=[('1', 'janeiro'), ('2', 'fevereiro'), ('3', 'março'), ('4', 'abril'), ('5', 'maio'), ('6', 'junho'), ('7', 'julho'), ('8', 'agosto'), ('9', 'setembro'), ('10', 'outubro'), ('11', 'novembro'), ('12', 'dezembro')], max_length=1)),
                ('comission', models.DecimalField(decimal_places=2, editable=False, max_digits=8)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='televendas.Seller', verbose_name='CPF')),
            ],
            options={
                'unique_together': {('seller', 'month')},
            },
        ),
    ]
