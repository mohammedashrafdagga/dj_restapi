from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator

# valid unique title 
# def validate_title(value):
#     qs = Product.objects.filter(title__iexact = value)
#     if qs.exists():
#         raise serializers.ValidationError(f'{value} is already exists')
#     return value

def validate_title_not_contains_hello(value):
    '''
        we need validate title not have hello value
    '''
    if 'hello' in value.lower():
        raise serializers.ValidationError('title must not contains hello word')
    return value


# build in in django
unique_title  = UniqueValidator(queryset=Product.objects.all(), lookup='iexact')