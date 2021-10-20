from django.db import models
from accounts.models import UserProfile
from business.models import *
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class ProductType(models.Model):
    product_name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    gtin_number = models.IntegerField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    guid = models.CharField(max_length=255, primary_key=True)
    manufacture_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(auto_now_add=True)
    lot_number = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    previous_owner = models.ForeignKey(Company, on_delete=models.CASCADE)
    current_owner = models.ForeignKey(Company, on_delete=models.CASCADE)

