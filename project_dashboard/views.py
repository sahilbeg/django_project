from django.shortcuts import render
from .models import App

def dashboard(request):
    apps = App.objects.all()
    return render(request, 'project_dashboard/dashboard.html', {'apps': apps})
