from product.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.serializers import ProductSerializer


@api_view(['GET'])  # list of method that allow access in this api view
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by('?').first()
    data = {}
    if instance:
        # clean up way
        data = ProductSerializer(instance).data
    return Response(data)
