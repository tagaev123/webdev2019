from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from shop.models import Category
from shop.serializers import CategorySerializer, ProductSerializer, CategorySerializer2

""" def category_list(request):
    categories = Category.objects.all()
    json_categories = [c.to_json() for c in categories]
    data = {
        'categories': json_categories
    }
    return JsonResponse(data, safe=False)

def category_detail(request, pk):
    try:
        c = Category.objects.get(id=pk)
    except Category.DoesNotExist as e:
        error = {
            'error': str(e)
        }
        return JsonResponse(error, safe=False)
    return JsonResponse(c.to_json())

def category_products(request, pk):
    try:
        c = Category.objects.get(id=pk)
    except Category.DoesNotExist as e:
        error = {
            'error': str(e)
        }
        return JsonResponse(error, safe=False)

    products = c.product_set.all()
    products1 = [c.to_json() for c in products]
    data = {
        'data': products1
    }
    return JsonResponse(data, safe = False) """

@csrf_exempt
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = CategorySerializer2(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors)

@csrf_exempt
def category_detail(request, pk):
    try:
        category = Category.objects.get(id=pk)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return JsonResponse(serializer.data, status=200)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = CategorySerializer(instance=category, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse( {},status=204)


def category_products(request, pk):
    try:
        category = Category.objects.get(id=pk)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    products = category.product_set.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)


