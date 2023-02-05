from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field = 'pk',
        read_only=True
    )
    title = serializers.CharField(read_only = True)
    
    
class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only = True)
    user_id = serializers.IntegerField(read_only = True, source = 'id')
    # other_product = serializers.SerializerMethodField(read_only = True)
    
    
    # def get_other_product(self, obj):
    #     qs = obj.product_set.all()
    #     return UserProductInlineSerializer(qs, context = self.context, many=True).data
    

class UserPublicModelSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            # 'pk',
            'name',
        ]
        
    def get_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'