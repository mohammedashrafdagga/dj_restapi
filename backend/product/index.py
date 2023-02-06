from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from .models import Product

@register(Product)
class ProductIndex(AlgoliaIndex):
    fields = [
        'user',
        'title',
        'content',
        'price',
        'public'
    ]

    tags = 'get_tag_lit'