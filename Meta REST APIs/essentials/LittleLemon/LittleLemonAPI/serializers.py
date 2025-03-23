from rest_framework import serializers
from .models import MenuItem, Category
from decimal import Decimal
import bleach

# SERIALIZER CLASS
# class MenuItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=6, decimal_places=2)
#     inventory = serializers.IntegerField()

# MODEL SERIALIZER CLASS / RELATIOINSHIP SERIALIZERS
class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']
class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory') # Changing the Iventory name to stock only user display.
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax') # How to add new field only user display
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    #Method 3 of validation - validate_field()
    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError('Stock cannot be negative')
        return value
    def validate_title(self, value):
        return bleach.clean(value)
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category', 'category_id']
        #validations methods 2
        extra_kwargs = {
            'price': {'min_value':1},
            # 'stock': {'source':'inventory', 'min_value':0} - Didn't work method 2 when using source
        }

    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)
