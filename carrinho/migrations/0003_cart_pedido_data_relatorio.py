# Generated by Django 3.2.10 on 2022-02-05 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0002_alter_cart_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='pedido_data_relatorio',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
