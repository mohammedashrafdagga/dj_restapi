
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('api.urls')),  # localhost:8000/api
    path('api/product/', include('product.urls')), # localhost:8000/api/product/
    path('api/search/', include('search.urls')),
    path('api/v2/', include('restapi.router')),
]
