from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project_dashboard.urls')),
    path('polls/', include('polls.urls')),
    path('project_management/', include('project_management.urls')),
]
