from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TypeView, TypeDetailView, EventDetailView, PersonDetailView

router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),

    path("types/", TypeView.as_view({'get': 'get_types'})),
    path("types/<int:pk>/", TypeDetailView.as_view({'get': 'get_detail_type'})),

    path("events/<int:pk>/", EventDetailView.as_view({'get': 'get_detail_event'})),

    path("persons/<int:pk>/", PersonDetailView.as_view({'get': 'get_detail_person'})),
]
