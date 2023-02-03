from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail', lookup_field = 'pk'
    )
    
    class Meta:
        model = Product
        fields = [
            'edit_url',
            'url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]

    def get_edit_url(self, obj):
        request = self.context.get('request') #request 
        if request is None:
            return None
        return reverse('product-update', kwargs={'pk': obj.pk}, request=request)
    
    
    def get_my_discount(self, obj):
        #  get my_discount method represent my_discount serializer filed
        # check is onj is instance from Product
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()  # return get_discount model method
