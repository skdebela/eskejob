from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.viewsets import ModelViewSet

from applications.filters import ApplicationFilter
from applications.models import Application
from applications.serializers import ApplicationSerializer


class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    search_fields = ["job__name", "job__created_by__full_name"]
    filterset_class = ApplicationFilter
    ordering_fields = [
        "job__name",
        "job__created_by__full_name",
        "applied_at",
        "job__created_at",
        "staus",
    ]

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="ordering",
                type=str,
                description="Field to order by (user prefix '-' for descending order).",
                enum=ordering_fields + [f"-{field}" for field in ordering_fields],
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
