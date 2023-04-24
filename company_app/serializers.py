from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Employee, Department


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    employee_count = serializers.IntegerField()
    salary_count = serializers.IntegerField()
    class Meta:
        model = Department
        fields = ['id', 'name', 'connection']
