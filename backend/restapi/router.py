from rest_framework.routers import DefaultRouter
from product.viewsets import ProductGenericsViewset


router = DefaultRouter()
router.register('products', ProductGenericsViewset, basename='products')

urlpatterns = router.urls