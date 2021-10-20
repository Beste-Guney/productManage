import product as product
from django.db import models
from accounts.models import UserProfile


# Create your models here.
class ActionLog(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    payload = models.CharField(max_length=255)


class Company(models.Model):
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12)
    logo = models.CharField(max_length=255)
    tax_office = models.CharField(max_length=255)
    tax_number = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='created_by')
    company_type = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)



