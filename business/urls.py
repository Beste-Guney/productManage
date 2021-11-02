from django.urls import path
from .api_views import *

urlpatterns = [
    path('companies/', CompanyAPIView.as_view()),
    path('companies/<int:id>', CompanyAPIView.as_view()),
    path('action_logs/', ActionLogAPIView.as_view()),
    path('action_logs/<int:id>', ActionLogAPIView.as_view())    
]