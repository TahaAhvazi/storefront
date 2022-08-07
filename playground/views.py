from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, Order, Customer
from django.db.models import Value, F, Func, ExpressionWrapper,DecimalField

def say_hello(request):
    discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    queryset = Product.objects.annotate(
        discounted_price =  discounted_price
    )
    return render(request, 'hello.html', {'name': 'Mosh', 'result': list(queryset)})
