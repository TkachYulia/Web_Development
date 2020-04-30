from django.http.response import JsonResponse, HttpResponse
from api.models import Product, Category


def products(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def product(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    return JsonResponse(product.to_json())


def categories(request, id):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)


def category(request, category_id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    return JsonResponse(category.to_json())


def category_product(request, category_id):
    try:
        products = Product.objects.filter(category_id=category_id)
        products_json = [product.to_json() for product in products]
        return JsonResponse(products_json, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)})
