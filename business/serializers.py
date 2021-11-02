from django.db.models import fields
from rest_framework import serializers
from .models import Company
from .models import ActionLog


class ActionLogSerializer(serializers.ModelSerializer):
    '''user = serializers.RelatedField(source='user', read_only=True)
    action_type = serializers.CharField(max_length=255)
    url = serializers.CharField(max_length=255)
    payload = serializers.CharField(max_length=255)'''

    class Meta:
        model = ActionLog
        fields = ('__all__')

class CompanySerializer(serializers.ModelSerializer):
    '''company_name = serializers.CharField(max_length=255)
    adress = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=12)
    logo = serializers.CharField(max_length=255)
    tax_office = serializers.CharField(max_length=255)
    tax_number = serializers.CharField(max_length=255)
    date_joined = serializers.DateTimeField(auto_now_add=True)
    created_by = serializers.RelatedField(source='created_by', read_only=True)
    company_type = serializers.CharField(max_length=255)
    is_active = serializers.BooleanField(default=True)'''

    class Meta:
        model = Company
        fields = ('__all__')