from rest_framework import viewsets, mixins
from .models import Product
from .serializers import ProductSerializer


class ProductViewset(viewsets.ModelViewSet):
    
    '''
        Get - List
        Get - retrieve 
        post - create new instance
        put - update instance
        patch - partial update
        delete - delete Instance
    '''
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    
class ProductGenericsViewset(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin, 
    viewsets.GenericViewSet):
    '''
    Get - List
    Get - retrieve 
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'