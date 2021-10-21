from django.db import models
from accounts.models import UserProfile
from business.models import Company
from owlready2 import *

# ontology location
onto = get_ontology("./ontology.owl")

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

    __original_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_name = self.category_name

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)
        if self.__original_name:
            original_onto_name = CategoryOnto(self.__original_name)
            original_onto_name.name = self.category_name
            onto.save(file='./ontology.owl')
        else:
            new_category = CategoryOnto(self.category_name)
        onto.save(file='./ontology.owl')


class ProductType(models.Model):
    product_name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    gtin_number = models.IntegerField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)

    __original_name = None
    __original_category = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_name = self.product_name

    def save(self, *args, **kwargs):
        super(ProductType, self).save(*args, **kwargs)
        if self.__original_name:
            original_onto_name = ProductTypeOnto(self.__original_name)
            original_onto_name.name = self.product_name
            original_category = CategoryOnto(self.category.category_name)
            original_onto_name.has_category = [original_category]
        else:
            product_type_onto = ProductTypeOnto(self.product_name)
            original_category = CategoryOnto(self.category.category_name)
            product_type_onto.has_category = [original_category]
        onto.save(file='./ontology.owl')


class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    guid = models.CharField(max_length=255, primary_key=True)
    manufacture_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(auto_now_add=True)
    lot_number = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    previous_owner = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='pre_owner', null=True)
    current_owner = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='cur_owner', null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        product_onto = ProductOnto(self.product_type.product_name + self.guid)
        product_type_onto = ProductTypeOnto(self.product_type.product_name)
        product_onto.has_product_type = [product_type_onto]
        onto.save(file='./ontology.owl')


class ItemLog(models.Model):
    previous_state = models.CharField(max_length=255)
    current_state = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
