from django.urls import path
from . import views

app_name = 'project_management'
urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('employee/<int:employee_id>/', views.employee_detail, name='employee_detail'),
]
