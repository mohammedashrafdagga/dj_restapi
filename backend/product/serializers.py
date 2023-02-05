from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from .validators import unique_title, validate_title_not_contains_hello

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail', lookup_field = 'pk'
    )
    
    title = serializers.CharField(validators = [unique_title, validate_title_not_contains_hello])
    # using source
    name = serializers.CharField(source = 'title', read_only = True)
    # also fk such as get email from user
    # email = serializers.EmailField(source = 'user.email', read_only = True)
    class Meta:
        model = Product
        fields = [
            'edit_url',
            'url',
            # 'email',
            'pk',
            'title',
            'name',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]
        
    # def validate_<filed_name>(self, value):  syntax
    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(user = request.user, title__iexact = value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f'{value} is already exists')
    #     return value
        
        
    # def create(self, validated_data):
    #     # return Product.objects.create(**validated_data)
    #     email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     print(email, obj)
    #     return obj
    
    # def update(self, instance, validated_data):
    #     # instance.title = validated_data.get('title')
    #     # email = validated_data.pop('email')
    #     return super().update(instance, validated_data)

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
