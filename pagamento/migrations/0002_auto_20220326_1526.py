# Generated by Django 3.2.10 on 2022-03-26 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
        ('pagamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetodosDePagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_metodo_de_pagamento', models.CharField(max_length=50)),
                ('restaurante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.restaurante')),
            ],
        ),
        migrations.DeleteModel(
            name='Pagamento',
        ),
    ]
