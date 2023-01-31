from product.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.serializers import ProductSerializer


@api_view(['GET', 'POST'])  # list of method that allow access in this api view
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # print(serializer)
        instance = serializer.save()
        return Response(serializer.data)
    return Response({
        'invalid': 'something is wrong!!'}, status=400)
