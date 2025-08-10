from django.contrib.auth import get_user_model
from djoser.views import UserViewSet as DjoserUserViewSet
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from users.filters import UserFilter
from users.serializers import (
    UserCreateSerializer,
)

User = get_user_model()


class UserViewSet(DjoserUserViewSet):
    queryset = User.objects.all()
    filterset_class = UserFilter
    search_fields = ["email", "first_name", "last_name"]
    ordering_fields = [
        "email",
        "first_name",
        "last_name",
    ]

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="ordering",
                type=str,
                location=OpenApiParameter.QUERY,
                description="Field to order by (use prefix '-' for descending order).",
                enum=ordering_fields + [f"-{field}" for field in ordering_fields],
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def create(self, request, *args, **kwargs):
        pass

    @action(
        detail=False,
        methods=["post"],
        url_path="signup",
        serializer_class=UserCreateSerializer,
        permission_classes=[AllowAny],
    )
    def signup(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
