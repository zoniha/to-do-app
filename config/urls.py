from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('control/', admin.site.urls),
    path('', include('todo_app.urls')),
]
