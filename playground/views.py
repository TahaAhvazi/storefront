from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, Order, Customer
from tags.models import TaggedItem
from django.db.models import Value, F, Func, ExpressionWrapper,DecimalField
from django.contrib.contenttypes.models import ContentType

def say_hello(request):
    return render(request, 'hello.html', {'name': 'Mosh',})
