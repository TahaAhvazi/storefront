from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, Order, Customer
from tags.models import TaggedItem
from django.db.models import Value, F, Func, ExpressionWrapper,DecimalField
from django.contrib.contenttypes.models import ContentType

def say_hello(request):
    content_type = ContentType.objects.get_for_model(Product) # This gonna be the Product ID in the contenttype table in the DataBase
    queryset=TaggedItem.objects.select_related('tag').filter(
        content_type=content_type,
        object_id = 1
    )
    return render(request, 'hello.html', {'name': 'Mosh', 'result': list(queryset)})
