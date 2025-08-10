from django_filters import rest_framework as filters

from jobs.models import Job
from users.models import User


class JobFilter(filters.FilterSet):
    class Meta:
        model = Job
        fields = []

    status = filters.ChoiceFilter(
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
