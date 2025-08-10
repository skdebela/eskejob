import os

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

from core.models import BaseModel
from jobs.models import Job

User = get_user_model()


def upload_resume_to(instance, filename):
    name, ext = os.path.splitext(filename)
    ext = ext.lower()
    if ext not in [".pdf", ".docx"]:
        raise ValidationError("Unsupported file type, please upload a PDF or DOCX file")

    return f"resumes/{instance.job.id}/{instance.applicant.id}/{name}{ext}"


class Application(BaseModel):
    STATUS_CHOICES = (
        ("applied", "Applied"),
        ("reviewed", "Reviewed"),
        ("interviewed", "Interviewed"),
        ("rejected", "Rejected"),
        ("hired", "Hired"),
    )
    applicant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="applications",
        limit_choices_to={"role": "applicant"},
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    resume_link = models.FileField(upload_to=upload_resume_to)
    cover_letter = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default="applied")
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant} - {self.job}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["applicant", "job"], name="unique_applicant_job"
            )
        ]
