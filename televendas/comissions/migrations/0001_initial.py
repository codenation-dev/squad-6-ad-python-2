# Generated by Django 2.2.2 on 2019-06-30 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlanoComissoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentagem_menor', models.IntegerField(max_length=3)),
                ('valor_minimo', models.FloatField(max_length=20)),
                ('porcentagem_maior', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('endereco', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=20)),
                ('idade', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.CharField(max_length=30)),
                ('plano_de_comissoes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comissions.PlanoComissoes')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(max_length=30)),
                ('valor_vendas', models.FloatField(max_length=20)),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comissions.Vendedor')),
            ],
        ),
    ]
