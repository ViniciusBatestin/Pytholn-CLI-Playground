from django.db import models

# Create your models here.
# MenuCategory
# Menu
# EXERCISE WORKING WITH FORMS **********
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

class Person(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()



# MODEL FORM STUDY *******************
# class Logger(models.Model):
#     first_name = models.CharField(max_length = 200)
#     last_name = models.CharField(max_length = 200)
#     time_log = models.TimeField(help_text='Enter the exact time')




# MENU CATEGORY STUDY *****************

# class MenuCategory(models.Model):
#     menu_category_name = models.CharField(max_length = 200)

# class Menu(models.Model):
#     menu_item = models.CharField(max_length = 200)
#     price = models.IntegerField()
#     category_id = models.ForeignKey(
#         MenuCategory,
#         on_delete=models.PROTECT,
#         default=None,
#         related_name="category_name")

# class Customer(models.Model):
#     name = models.CharField(max_length=255)

# class Vehicle(models.Model):
#     name = models.CharField(max_length=255)
#     customer = models.ForeignKey(Customer,
#                                  on_delete=models.CASCADE,
#                                  related_name='Vehicle'
#                                  )
