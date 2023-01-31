from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]

    def get_my_discount(self, obj):
        #  get my_discount method represent my_discount serializer filed
        # check is onj is instance from Product
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()  # return get_discount model method
