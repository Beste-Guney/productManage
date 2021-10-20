from django.db import models
from product.models import *
from accounts.models import *


# Create your models here.
class ItemLog(models.Model):
    previous_state = models.CharField(max_length=255)
    current_state = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class ActionLog(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    payload = models.CharField(max_length=255)


class Company(models.Model):
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField()
    phone_number = models.CharField(max_length=12)
    logo = models.CharField(max_length=255)
    tax_office = models.CharField(max_length=255)
    tax_number = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    company_type = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)



