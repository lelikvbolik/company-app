from django.db import models


class Employee(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    photo = models.ImageField(max_length=100)
    position = models.CharField(max_length=200)
    salary = models.IntegerField()
    age = models.CharField(max_length=100)
    department = models.OneToOneField('Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name


class Department(models.Model):
    name = models.CharField(max_length=200)
    connection = models.CharField(max_length=200)

    def __str__(self):
        return self.name
