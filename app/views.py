from django.shortcuts import render,redirect
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

from django.utils import timezone   
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


# def home(request):
#     users = Employee_register.objects.all()
#     return render(request, 'home.html',{'users':users})

from .models import *
def admin_data(request):
    # for employee in Employee_register:
    name = Employee_register.objects.all()
    
    print(name)
    return render(request,'home.html', {'name':name})
time = timezone.now().time()
import datetime



def attendence(request):
    time = datetime.datetime.now()
    if request.method == 'POST':
            employe = Employee_register.objects.get(id=3)
            action = request.POST.get('action')
            if action == 'checkin':
                obj = Employee_Attendence.objects.create(name=employe,check_in= time)
                obj.save()
                return redirect('home')
            elif action == 'checkout':
                obj = Employee_Attendence.objects.create(name=employe,check_out= time)
                obj.save()
                return redirect('home')
    return render(request,'attendence.html')


def emp(request):
    obj = Employee_register.objects.get(id=3)
    status =  Employee_Attendence.objects.filter(name=obj)
    
    return render (request,'dash.html',{'x':status})