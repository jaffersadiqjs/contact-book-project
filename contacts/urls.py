from django.urls import path
from . import views

urlpatterns = [
    path("", views.contact_list, name="contact_list"),
    path("add/", views.add_contact, name="add_contact"),
    path("feedback/", views.feedback_view, name="feedback"),
]
