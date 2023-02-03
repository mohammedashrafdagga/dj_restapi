from rest_framework import permissions
from .permissions import IsStaffProductEditor

class StaffPermissionMixins():
    permission_classes = [permissions.IsAdminUser, IsStaffProductEditor]