from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from . import serializers
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny

class EmployeeViewSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10

class EmployeeViewSet(viewsets.ModelViewSet):
    pagination_class = EmployeeViewSetPagination
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['last_name', 'department_id']
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(last_name=self.request.user)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(last_name=self.request.user)