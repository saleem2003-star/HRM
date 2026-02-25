from rest_framework import serializers
from .models import Employee_register

class Employee_serializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_register
        fields = '__all__'
