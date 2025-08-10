from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet

from jobs.filters import JobFilter
from jobs.models import Job
from jobs.permissions import IsCreatorOrReadOnly
from jobs.serializers import JobSerializer


class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated, IsCreatorOrReadOnly]
    search_fields = ["name", "description", "location"]
    filterset_class = JobFilter
    ordering_fields = [
        "name",
        "created_by__full_name",
        "created_at",
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

    def create(self, request, *args, **kwargs):
        user = request.user
        if not user.role == "company":
            raise PermissionDenied("Unauthorized to perform this action")

        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.validated_data["created_by"] = user
        serializer.save()
