from rest_framework import generics, mixins
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from api.mixins import StaffPermissionMixins, UserQuerySetMixins
# create product api view


class ProductListCreateAPIView(
    UserQuerySetMixins,
    StaffPermissionMixins,
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        # email = serializer.validated_data.pop('email')
        if content is None:
            content = title
        serializer.save(content=content, user = self.request.user)

    # def get_queryset(self, *args, **kwargs):
    #     user = self.request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     qs = super().get_queryset(*args, **kwargs)
    #     return qs.filter(user = user)

# detail View
class ProductDetailApiView( 
                            UserQuerySetMixins,
                           StaffPermissionMixins,
                           generics.RetrieveAPIView
                           ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Update View
class ProductUpdateApiView(
     UserQuerySetMixins,
     StaffPermissionMixins,
     generics.UpdateAPIView
     ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


# destroy View
class ProductDeleteApiView( 
                            UserQuerySetMixins,
                           StaffPermissionMixins,
                           generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    # perform delete instance
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


# Using Mixins View
# (This Class merge List, Retrieve and Create Class API View) in One Class

class ProductMixinsView(
     UserQuerySetMixins,
     StaffPermissionMixins,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # get
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = 'From mixins updated your content'
        serializer.save(content=content)


# Function Based View (List, Retrieve, Create)
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    # request -> get (detail or list)
    if method == 'GET':
        if pk:  # not None -> detail View
            qs = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(qs).data
            return Response(data)

        # list View
        qs = Product.objects.all()
        data = ProductSerializer(qs, many=True).data
        return Response(data)

    elif method == 'POST':  # create new instance from Product
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
        return Response(serializer.data)


# for more cleanup, Move all Variable Here
# list and create product view
product_list_create_view = ProductListCreateAPIView.as_view()

# Detail view
product_detail_view = ProductDetailApiView.as_view()

# Update View
product_update_view = ProductUpdateApiView.as_view()

# Delete View
product_delete_view = ProductDeleteApiView.as_view()


# Product Mixins View
product_mixin_view = ProductMixinsView.as_view()
