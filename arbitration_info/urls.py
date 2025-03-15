from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cases/", include("cases.urls")),  # Ensure this is correctly included
]
