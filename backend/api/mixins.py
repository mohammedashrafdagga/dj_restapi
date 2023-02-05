from rest_framework import permissions
from .permissions import IsStaffProductEditor
from product.models import Product

class StaffPermissionMixins():
    permission_classes = [permissions.IsAdminUser, IsStaffProductEditor]
    
    
    
class UserQuerySetMixins():
    def get_queryset(self, *args, **kwargs):
        user = self.request.user

        if not user.is_authenticated:
            return Product.objects.none()
        qs = super().get_queryset(*args, **kwargs)
        
        # if user.is_staff:
        #     return qs
        return qs.filter(user = user)
