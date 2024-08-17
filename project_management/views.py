from django.shortcuts import render, get_object_or_404
from .models import Employee, ProjectAssignment

def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    assignments = ProjectAssignment.objects.filter(employee=employee)
    return render(request, 'project_management/employee_detail.html', {
        'employee': employee,
        'assignments': assignments
    })
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'project_management/employee_list.html', {'employees': employees})
