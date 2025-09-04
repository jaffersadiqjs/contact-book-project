from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path("contacts/", include("contacts.urls")),
    path("", lambda request: redirect("contact_list")),  # 👈 redirect root → contacts
]
