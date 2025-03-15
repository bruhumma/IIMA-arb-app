from django.urls import path
from .views import case_lookup

urlpatterns = [
    path("", case_lookup, name="case_index"),  # Loads index.html
    path("lookup/", case_lookup, name="case_lookup"),  # API for fetching cases
]
