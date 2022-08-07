from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, Order, Customer
from django.db.models import Value, F, Func

def say_hello(request):
    queryset = Customer.objects.annotate(
        full_name = Func(F('first_name'), Value(' '), F('last_name'), function=('CONCAT'))
    )
    return render(request, 'hello.html', {'name': 'Mosh', 'result': list(queryset)})
