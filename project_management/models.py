from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=10, unique=True)
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.project_name

class ProjectAssignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee.full_name} - {self.project.project_name}"
