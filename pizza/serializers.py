from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers

from pizza.models import IngredientPizza, Pizza, Drink, OrderUser, OrderPizza, OrderDrink


class UserDetailInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']


class IngredientPizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientPizza
        fields = ['id', 'title']


class PizzaSerializer(serializers.ModelSerializer):
    ingredients = IngredientPizzaSerializer(many=True)

    class Meta:
        model = Pizza
        fields = ['id', 'title', 'ingredients', 'weight', 'description']


class PizzaCreateSerializer(serializers.ModelSerializer):
    ingredients = serializers.PrimaryKeyRelatedField(many=True, queryset=IngredientPizza.objects.all())

    class Meta:
        model = Pizza
        fields = ['id', 'title', 'ingredients', 'weight', 'description']


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'title']


class OrderUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderUser
        fields = "__all__"


class OrderDrinkSerializer(serializers.ModelSerializer):
    drink = serializers.PrimaryKeyRelatedField(queryset=Drink.objects.all(), source="drink_id")

    class Meta:
        model = OrderDrink
        fields = ["count", "note", "drink"]


class OrderPizzaSerializer(serializers.ModelSerializer):
    pizza = serializers.PrimaryKeyRelatedField(queryset=Pizza.objects.all(), source="pizza_id")

    class Meta:
        model = OrderPizza
        fields = ["count", "note", "pizza"]


class OrderUserCreateSerializer(serializers.ModelSerializer):
    order_item_pizza = OrderPizzaSerializer(many=True)
    order_item_drink = OrderDrinkSerializer(many=True)

    class Meta:
        model = OrderUser
        fields = "__all__"
        exclude_field = "owner_id"

    def save(self, owner_id):
        with transaction.atomic():
            order_pizza_list = []
            order_drink_list = []
            for order_pizza in self.validated_data["order_item_pizza"]:
                order_pizza_list.append(OrderPizza.objects.create(pizza=order_pizza["pizza_id"],
                                                                  count=order_pizza["count"],
                                                                  note=order_pizza["note"]))
            for order_drink in self.validated_data["order_item_drink"]:
                order_drink_list.append(OrderDrink.objects.create(pizza=order_drink["drink_id"],
                                                                  count=order_drink["count"],
                                                                  note=order_drink["note"]))

            order_user = OrderUser.objects.create(owner_id=owner_id,
                                                  order_status=self.validated_data["order_status"],
                                                  total_price=0,
                                                  type_order=self.validated_data["type_order"],
                                                  payment_method=self.validated_data["payment_method"],
                                                  payment_status=self.validated_data["payment_status"])
            order_user.order_item_pizza.add(*order_pizza_list)
            order_user.order_item_drink.add(*order_drink_list)
            return order_user
