from django.contrib import admin
from .models import Booking, Person
from django.contrib.auth.admin import UserAdmin
# Register your models here.
# admin.site.register(Menu)
# admin.site.register(MenuCategory)
# admin.site.register(Logger)


admin.site.register(Booking)
admin.site.register(Person)
