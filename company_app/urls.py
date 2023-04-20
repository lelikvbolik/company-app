from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('employees/', views.EmployeeList.as_view()),
    path('employees//', views.EmployeeDetail.as_view()),
    path('departments/', views.DepartmentList.as_view()),
    path('departments//', views.DepartmentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
