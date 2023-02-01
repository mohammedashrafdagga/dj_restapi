from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
# create product api view


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)


# list and create product view
product_list_create_view = ProductListCreateAPIView.as_view()

# detail View


class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_filed = id default


product_detail_view = ProductDetailApiView.as_view()


# Update View
class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


product_update_view = ProductUpdateApiView.as_view()


# destroy View
class ProductDeleteApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    # perform delete instance
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


product_delete_view = ProductDeleteApiView.as_view()


# Function Based View (List, Retrieve, Create)
# @api_view(['GET', 'POST'])
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method
#     # request -> get (detail or list)
#     if method == 'GET':
#         if pk:  # not None -> detail View
#             qs = get_object_or_404(Product, pk=pk)
#             data = ProductSerializer(qs).data
#             return Response(data)

#         # list View
#         qs = Product.objects.all()
#         data = ProductSerializer(qs, many=True).data
#         return Response(data)

#     elif method == 'POST':  # create new instance from Product
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content') or None
#             if content is None:
#                 content = title
#             serializer.save(content=content)
#         return Response(serializer.data)
