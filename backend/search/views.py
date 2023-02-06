from rest_framework import generics
from product.models import Product
from product.serializers import ProductSerializer
from rest_framework.response import Response
from . import client

class SearchListView(generics.GenericAPIView):
    def get(self,request, *args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user
        query = request.GET.get('q')
        tags = request.GET.get('tags') or None
        public = str(request.GET.get('public')) != '0'
        if not query:
            return Response({'detail':'not have any data'}, status=400)

        results = client.perform_search(query, tags=tags, user = user, public = public)
        return Response(results)
    
    
    
    
class SearchOldListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        results = Product.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)
        return results
