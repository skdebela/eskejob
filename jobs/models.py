from django.contrib.auth import get_user_model
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models

from core.models import BaseModel

User = get_user_model()


class Job(BaseModel):
    STATUS_CHOICES = (
        ("open", "Open"),
        ("closed", "Closed"),
    )
    title = models.TextField(
        validators=[MinLengthValidator(1), MaxLengthValidator(1000)]
    )
    description = models.TextField(
        validators=[MinLengthValidator(20), MaxLengthValidator(2000)]
    )
    location = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="open")
    created_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="jobs_created_by"
    )
    created_at = models.DateTimeField(auto_now_add=True)
