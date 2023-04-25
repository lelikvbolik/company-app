from rest_framework import serializers

from .models import Employee, Department


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    employee_count = serializers.IntegerField(read_only=True)
    total_salary = serializers.IntegerField(read_only=True)

    class Meta:
        model = Department
        fields = '__all__'
