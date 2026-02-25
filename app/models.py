from django.db import models

# Create your models here.
class Employee_register(models.Model):
    name = models.CharField(max_length=250)
    role = models.CharField(max_length = 20)
    def __str__(self):
        return self.name
    
class Admin(models.Model):
    model = models.ForeignKey(Employee_register,on_delete=models.CASCADE)

# class Employee_register(models.Model):
#     employee_name = models.ForeignKey(Employee_register,on_delete=models.CASCADE)
#     def __str__(self):
#         return self.employee_name
    

class Employee_Documents(models.Model):
    employee_documents = models.ForeignKey(Employee_register,on_delete=models.CASCADE)
    doc_type = models.CharField(max_length=60, choices=[('Aadhar','Aadhar'),('Pan','Pan'),('SSC','SSC'),('Photo','Photo'),('Inter','Inter'),('Bank_details','Bank_details'),('Graduation','Graduation')])
    file = models.FileField()

class Employee_Attendence(models.Model):
    name = models.ForeignKey(Employee_register,on_delete=models.CASCADE)
    attendence = models.DateTimeField(auto_now_add=True)
    check_in = models.TimeField()
    check_out = models.TimeField(null=True,blank=True)

class Employee_Payroll(models.Model):
    name = models.ForeignKey(Employee_register,on_delete=models.CASCADE)
    payslips = models.FileField()
    
class Employee_BreakManagement(models.Model):
    name = models.ForeignKey(Employee_register,on_delete=models.CASCADE)
    break_in = models.DateTimeField()
    break_out = models.DateTimeField()


   
 
    
    
    
    
    