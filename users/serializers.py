from django.contrib.auth import get_user_model
from djoser import serializers as djoser_serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as BaseTokenObtainPairSerializer,
)

User = get_user_model()


class TokenObtainPairSerializer(BaseTokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["role"] = user.role
        return token


class UserCreateSerializer(djoser_serializers.UserCreateSerializer):
    class Meta(djoser_serializers.UserCreateSerializer.Meta):
        model = User
        fields = [
            "full_name",
            "email",
            "role",
            "password",
        ]


class UserSerializer(djoser_serializers.UserSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "full_name",
            "email",
            "role",
        ]
