from django.contrib.auth.models import User
from django.db import models


class IngredientPizza(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.title}'


class Pizza(models.Model):
    title = models.CharField(max_length=64, unique=True)
    ingredients = models.ManyToManyField(IngredientPizza)
    weight = models.PositiveIntegerField(default=0)
    description = models.TextField(max_length=1024)

    def __str__(self):
        return f'{self.title}'


class Drink(models.Model):
    title = models.CharField(max_length=64, unique=True)
    description = models.TextField(max_length=1024)

    def __str__(self):
        return f'{self.title}'


class OrderPizza(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    note = models.CharField(max_length=512)

    def __str__(self):
        return f'{self.id}'


class OrderDrink(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    note = models.CharField(max_length=512)

    def __str__(self):
        return f'{self.id}'


class OrderUser(models.Model):
    choice_order_status = (
       ('accepted', 'Accepted'),
       ('process', 'In process'),
       ('ready', 'Ready'),
    )
    choice_type_order = (
       ('restaurant', 'In a restaurant'),
       ('delivery', 'Delivery'),
    )
    choice_payment_method = (
       ('cash', 'Cash'),
       ('cart', 'Cart'),
    )
    choice_payment_status = (
       ('success', 'Success'),
       ('error', 'Error'),
       ('process', 'In process'),
    )
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.PositiveBigIntegerField()
    order_item_pizza = models.ManyToManyField(OrderPizza, related_name='user_orders', blank=True)
    order_item_drink = models.ManyToManyField(OrderDrink, related_name='user_orders', blank=True)
    order_status = models.CharField(max_length=16, choices=choice_order_status, default='accepted')
    type_order = models.CharField(max_length=16, choices=choice_type_order, blank=False, null=False)
    date_create = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=16, choices=choice_payment_method, blank=False, null=False)
    payment_status = models.CharField(max_length=16, choices=choice_payment_status, default='In process')

    def __str__(self):
        return f'{self.id}'
