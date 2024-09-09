from django.db import models
from django.contrib.auth.models import User
from mechanics.models import Mechanic
from drivers.models import Driver


class ServiceRequest(models.Model):
    SERVICE_TYPES = [
        ("emergency", "Emergency"),
        ("custom", "Custom"),
        ("scheduled", "Scheduled"),
    ]
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Request by {self.driver.user.username} - Status: {self.status}"
