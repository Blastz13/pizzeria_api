from django.contrib import admin

from pizza.models import Pizza, Drink, OrderUser, OrderPizza, OrderDrink, IngredientPizza


@admin.register(IngredientPizza)
class IngredientPizzaAdmin(admin.ModelAdmin):
    pass


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    pass


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderUser)
class OrderUserAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderPizza)
class OrderPizzaAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderDrink)
class OrderDrinkAdmin(admin.ModelAdmin):
    pass
