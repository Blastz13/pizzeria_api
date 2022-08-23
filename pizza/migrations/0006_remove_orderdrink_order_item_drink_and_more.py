# Generated by Django 4.1 on 2022-08-20 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0005_remove_orderuser_order_item_drink_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdrink',
            name='order_item_drink',
        ),
        migrations.RemoveField(
            model_name='orderpizza',
            name='order_item_pizza',
        ),
        migrations.AddField(
            model_name='orderuser',
            name='order_item_drink',
            field=models.ManyToManyField(null=True, related_name='user_orders', to='pizza.drink'),
        ),
        migrations.AddField(
            model_name='orderuser',
            name='order_item_pizza',
            field=models.ManyToManyField(null=True, related_name='user_orders', to='pizza.pizza'),
        ),
    ]
