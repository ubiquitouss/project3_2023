# django_project/urls.py
from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
 path("admin/", admin.site.urls),
 path("accounts/", include("django.contrib.auth.urls")), #specially for creating accounts provided by django
 path("accounts/", include("accounts.urls")),
 path("", include("blog.urls")), # new
]
