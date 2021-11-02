from django.db.models import fields
from rest_framework import serializers
from .models import Category
from .models import ItemLog
from .models import ProductType
from .models import Product

class CategorySerializer(serializers.ModelSerializer):
    '''category_name = serializers.CharField(max_length=255)
    created_by = serializers.RelatedField(source='created_by', read_only=True)
    created_at = serializers.DateTimeField(auto_now_add=True)
    is_active = serializers.BooleanField(default=True)'''

    class Meta:
        model = Category
        fields = ('__all__')

    

class ProductTypeSerializer(serializers.ModelSerializer):
    '''product_name = serializers.CharField(max_length=255)
    image = serializers.CharField(max_length=255)
    category = serializers.RelatedField(source='category', read_only=True)
    created_by = serializers.RelatedField(source='created_by', read_only=True)
    created_at = serializers.DateTimeField()'''

    class Meta:
        model = ProductType
        fields = ('__all__')


class ProductSerializer(serializers.ModelSerializer):
    '''product_type = serializers.RelatedField(source='product_type', read_only=True)
    guid = serializers.CharField(max_length=255)
    manufacture_date = serializers.DateTimeField()
    expiration_date = serializers.DateTimeField()
    lot_number = serializers.CharField(max_length=255)
    state = serializers.CharField(max_length=255)
    previous_owner = serializers.RelatedField(source='previous_owner', read_only=True)
    current_owner = serializers.RelatedField(source='current_owner', read_onley=True)'''

    class Meta:
        model = Product
        fields = ('__all__')

    

class ItemLogSerializer(serializers.ModelSerializer):
    '''previous_state = serializers.CharField(max_length=255)
    current_state = serializers.CharField(max_length=255)
    product = serializers.RelatedField(source='product', read_only=True)
    date_time = serializers.DateTimeField()
    user = serializers.RelatedField(source='user', read_only=True)'''

    class Meta:
        model = ItemLog
        fields = ('__all__')