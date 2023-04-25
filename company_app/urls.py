from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employee', views.EmployeeViewSet)
router.register('department', views.DepartmentViewSet)
urlpatterns = router.urls
