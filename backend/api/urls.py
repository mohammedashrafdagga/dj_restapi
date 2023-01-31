from . import views
from django.urls import path


urlpatterns = [
    path('', views.api_home)  # localhost:8000/api/
]
