from django.shortcuts import render
from django.views import View
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


class CreateRuleView(View):
    def get(self, request):
        #creating the options
        context = {}
        classes = []
        class_and_variable = {}
        rules = []

        #list of onto classes
        for index, ontology in enumerate(onto.classes()):
            classes.append(ontology.name + '( ?' + chr(index + 97) + ')' )
            class_and_variable[ontology.name] = chr(index + 97)

        for index, rule in enumerate(onto.object_properties()):
            rules.append(rule.name + '( ?' + class_and_variable[rule.domain[0].name] + ', ?' + class_and_variable[rule.range[0].name] + ')')
        context = {'classes': classes, 'rules': rules}
        return render(request, 'test.html', context)

    def post(self, request):
        chosen_option = request.POST['first']
        print(chosen_option)


