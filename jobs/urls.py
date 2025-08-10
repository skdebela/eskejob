from django.urls import include, path
from rest_framework.routers import DefaultRouter

from jobs.views import JobViewSet

router = DefaultRouter()
router.register("jobs", JobViewSet, basename="jobs")

urlpatterns = [
    path("", include(router.urls)),
]
