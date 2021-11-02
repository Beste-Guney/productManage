from django.urls import path
from .api_views import *

urlpatterns = [
    path('products/', ProductAPIView.as_view()),
    path('products/<int:id>', ProductAPIView.as_view()),
    path('categories/', CategoryAPIView.as_view()),
    path('categories/<int:id>', CategoryAPIView.as_view()),
    path('product_types/', ProductTypeAPIView.as_view()),
    path('product_types/<int:id>', ProductTypeAPIView.as_view()),
    path('item_logs/', ItemLogAPIView.as_view()),
    path('item_logs/<int:id>', ItemLogAPIView.as_view())
]