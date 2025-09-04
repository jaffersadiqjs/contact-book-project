from django.db import models
from django.conf import settings
from django.core.mail import send_mail

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Send email to admin when new contact is added
        send_mail(
            subject="New Contact Added",
            message=f"A new contact was added:\n\nName: {self.name}\nEmail: {self.email}\nPhone: {self.phone}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
            fail_silently=True,
        )
