from django.db import models

# Create your models here.
class Employee_register(models.Model):
    name = models.CharField(max_length=250)
    role = models.CharField(max_length = 20)
    def __str__(self):
        return self.name