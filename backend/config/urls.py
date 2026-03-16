from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_home(request):
    return JsonResponse({"message": "Welcome to the Team Task Manager API! The engine is running."})

urlpatterns = [
    path('', api_home), # Show a message at the root URL (/)
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('api/teams/', include('teams.urls')),
    path('api/tasks/', include('tasks.urls')),
]
