
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('api.urls')),  # localhost:8000/api
    # localhost:8000/api/product/
    path('api/product/', include('product.urls')),
]
