from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
from .forms import ContactForm, FeedbackForm

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, "contacts/contact_list.html", {"contacts": contacts})

def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact_list")
    else:
        form = ContactForm()
    return render(request, "contacts/add_contact.html", {"form": form})

def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            send_mail(
                subject=f"Feedback from {name}",
                message=message,
                from_email=email,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=False,
            )
            return redirect("contact_list")
    else:
        form = FeedbackForm()
    return render(request, "contacts/feedback.html", {"form": form})
