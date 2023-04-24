from django.db import models

class Employee(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    photo = models.ImageField(max_length=100)
    position = models.CharField(max_length=200)
    salary = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name

class Department(models.Model):
    name = models.CharField(max_length=200, help_text='Enter name department')
    connection = models.CharField(max_length=200, help_text="Enter connection employee or department director")

    def __str__(self):
        return self.name

