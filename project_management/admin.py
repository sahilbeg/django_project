from django.contrib import admin
from .models import Employee, Project, ProjectAssignment

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'full_name', 'age', 'email', 'phone_number', 'designation')
    search_fields = ('full_name', 'employee_id')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'description')
    search_fields = ('project_name',)

@admin.register(ProjectAssignment)
class ProjectAssignmentAdmin(admin.ModelAdmin):
    list_display = ('employee', 'project')
    search_fields = ('employee__full_name', 'project__project_name')
