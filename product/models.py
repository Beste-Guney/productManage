from django.db import models
from accounts.models import UserProfile
from business.models import Company
from owlready2 import *

# ontology location
onto = get_ontology("http://test.org/onto.owl")

# ontology classes
with onto:
    class CategoryOnto(Thing):
        pass


    class ProductTypeOnto(Thing):
        pass


    class ProductOnto(Thing):
        pass


    class ItemLogOnto(Thing):
        pass

    class has_category(ProductTypeOnto >> CategoryOnto):
        pass

    class has_product_type(ProductOnto >> ProductTypeOnto):
        pass


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=255)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)
        new_category = CategoryOnto(self.category_name)


class ProductType(models.Model):
    product_name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    gtin_number = models.IntegerField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super(ProductType, self).save(*args, **kwargs)
        product_type_onto = ProductTypeOnto(self.product_name)
        product_type_onto.has_category.append(self.category.category_name)


class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    guid = models.CharField(max_length=255, primary_key=True)
    manufacture_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(auto_now_add=True)
    lot_number = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    previous_owner = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='pre_owner', null=True)
    current_owner = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='cur_owner', null=True)

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        product_onto = ProductOnto(self.product_type.product_name + self.guid)
        product_onto.has_product_type.append(self.product_type.product_name)



class ItemLog(models.Model):
    previous_state = models.CharField(max_length=255)
    current_state = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
