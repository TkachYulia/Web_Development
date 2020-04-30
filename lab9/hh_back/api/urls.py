from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('api/companies/', views.companies),
    path('api/companies/<int:id>/', views.company),
    path('companies/<int:id>/vacancies/', views.company_vacans),

    path('api/vacancies/', views.vacancies),
    path('api/vacancies/<int:id>/', views.vacancy),
    path('api/vacancies/top_ten/', views.top_vacancies)
]
