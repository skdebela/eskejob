from django_filters import rest_framework as filters

from applications.models import Application
from jobs.models import Job
from users.models import User


class ApplicationFilter(filters.FilterSet):
    application_status = filters.ChoiceFilter(
        field_name="status",
        help_text="Filter by status",
        choices=Application.STATUS_CHOICES,
    )
    job_status = filters.ChoiceFilter(
        field_name="status",
        help_text="Filter by status",
        choices=Job.STATUS_CHOICES,
    )
    company = filters.ModelChoiceFilter(
        field_name="created_by__id",
        help_text="Filter by the ID of company.",
        to_field_name="id",
        queryset=User.objects.filter(role="company"),
    )

    class Meta:
        model = Application
        fields = []
