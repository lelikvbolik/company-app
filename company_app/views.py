from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from . import serializers
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer

class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['last_name']

    def perform_create(self, serializer):
        serializer.save(last_name=self.request.user)

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

    def perform_create(self, serializer):
        serializer.save(last_name=self.request.user)

class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = serializers.DepartmentSerializer