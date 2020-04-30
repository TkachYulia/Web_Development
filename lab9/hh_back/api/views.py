from django.shortcuts import render

# Create your views here.

from api.models import Company, Vacancy
from django.http.response import JsonResponse


def companies(request):
    companies = Company.objects.all()
    companies_json = [company.short() for company in companies]
    return JsonResponse(companies_json, safe=False)


def company(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error', str(e)})
    return JsonResponse(company.to_json())


def company_vacans(request, id):
    try:
        vacancies = Vacancy.objects.filter(company_id=id).all()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)})


def vacancies(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.short() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancy(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(vacancy.to_json())


def top_vacancies(request):
    vacancies = Vacancy.objects.order_by("-salary")
    length = min(10, len(vacancies))
    vacancies_json = [vacancies[i].to_json() for i in range(length)]
    return JsonResponse(vacancies_json, safe=False)
