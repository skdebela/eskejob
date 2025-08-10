from django_filters import rest_framework as filters

from users.models import User


class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = []

    role = filters.ChoiceFilter(choices=User.ROLE_CHOICES)
