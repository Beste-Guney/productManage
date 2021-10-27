from django.db import models
from accounts.models import UserProfile
from business.models import Company
from owlready2 import *
from business.models import CompanyOnto

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


    class CompanyOnto(Thing):
        pass


    class has_category(ProductTypeOnto >> CategoryOnto):
        pass


    class has_product_type(ProductOnto >> ProductTypeOnto):
        pass


    class has_product(CompanyOnto >> ProductOnto):
        pass


    class product_category(ProductOnto >> CategoryOnto):
        pass

    rule = Imp()
    rule.set_as_rule(
        """ ProductOnto(?p), has_product_type(?p, ?d), has_category(?d, ?c) -> product_category(?p, ?c)""")

    cate_onto = CategoryOnto('cikolata')
    type_onto = ProductTypeOnto('bitter', has_category=[cate_onto])
    pro_onto = ProductOnto('bitter1', has_product_type=[type_onto])

    #sync_reasoner_pellet(infer_property_values=True, infer_data_property_values=True)
    print(str(rule))
    print(cate_onto)
    print(type_onto.has_category)
    print(pro_onto.has_product_type)
    print('jfdhjdhdjshf')
    print(pro_onto.product_category)


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
        destroy_entity(product_onto)
        product_onto2 = ProductOnto(self.product_type.product_name + self.guid)
        company_onto_current = CompanyOnto(self.current_owner.company_name)
        company_onto_current.has_product.append(product_onto2)
        product_type_onto = ProductTypeOnto(self.product_type.product_name)
        product_onto2.has_product_type = [product_type_onto]
        onto.save(file='./ontology.owl')


class ItemLog(models.Model):
    previous_state = models.CharField(max_length=255)
    current_state = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
