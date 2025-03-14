from django.db import models

# Create your models here.
# MenuCategory
# Menu

class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length = 200)

class Menu(models.Model):
    menu_item = models.CharField(max_length = 200)
    price = models.IntegerField()
    category_id = models.ForeignKey(
        MenuCategory,
        on_delete=models.PROTECT,
        default=None,
        related_name="category_name")

class Customer(models.Model):
    name = models.CharField(max_length=255)

class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 related_name='Vehicle'
                                 )
