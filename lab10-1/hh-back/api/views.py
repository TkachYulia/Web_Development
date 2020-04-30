from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import Vacancy, Company




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
        company = Company.objects.get(id=id)
        vacancies = company.vacancy_set.all()
        vacancies_json = [v.to_json() for v in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    except:
        return JsonResponse({"error": "No vacancies"})


def vacancies(request):
    try:
        vacancies = Vacancy.objects.all()
        vacancies_json = [v.to_json() for v in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    except:
        return JsonResponse({"error": "No vacancies"})

def vacancy(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
        vacancy_json = vacancy.to_json()
        return JsonResponse(vacancy_json, safe=False)
    except:
        return JsonResponse({"error": "No vacancy"})

def top_vacancies(request):
    try:
        vacancies = Vacancy.objects.order_by('-salary')
        vacancies_json = []
        
        counter = 0
        for v in vacancies:
            if(counter >= 10):
                break
            vacancies_json.append(v.to_json())
            counter += 1
        return JsonResponse(vacancies_json, safe=False)
    except:
        return JsonResponse({"error": "No vacancies"})


