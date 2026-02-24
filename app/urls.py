from django.urls import path
from .views import employee_data

urlpatterns = [
    path("employees/", employee_data),
    
]