from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [

    path('api/products', views.products),
    path('api/product/<int:id>', views.product),
    path('api/categories', views.categories),
    path('api/categories/<int:id>', views.category),
    path('api/categories/<int:id>/products', views.category_product)
]
