from django.shortcuts import render
from .models import Employee_register
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Employee_serializer

@api_view(['GET','POST'])
# def student_list(request):
#     if request.method == 'GET':
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def employee_data(request):
    if request.method == 'GET':
        employees = Employee_register.objects.all()
        serializer = Employee_serializer(employees, many = True)
        return Response(serializer.data)
    # if request.method == 'POST':
    #     serializer = Employee_serializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         Employee_register.objects.create(**serializer.validated_data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['PUT','DELETE'])
def employee_update(request,id):
    try :
        employee =  Employee_register.objects.get(id=id)
    except:
        return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = Employee_serializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    if request.method == 'DELETE':
        employee.delete()
        return Response({"message": "Deleted"})