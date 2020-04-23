from django.urls import path
from api import views
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('companies/', views.companies),
    path('companies/<int:id>/', views.company),
    path('companies/<int:id>/vacancies/', views.company_vacans),
    path('login/', obtain_jwt_token),
]