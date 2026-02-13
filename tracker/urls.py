from django.urls import path

from tracker.apps import TrackerConfig
from tracker.views import (
    HabitListView,
    HabitCreateApiView,
    HabitDestroyApiView,
    HabitListApiView,
    HabitRetrieveApiView,
    HabitUpdateApiView,
)

app_name = TrackerConfig.name

urlpatterns = [
    path("habit/create/", HabitCreateApiView.as_view(), name="habit-create"),
    path("habit/", HabitListApiView.as_view(), name="habit-list"),
    path("habit/<int:pk>/", HabitRetrieveApiView.as_view(), name="habit-retrieve"),
    path("habit/<int:pk>/update/", HabitUpdateApiView.as_view(), name="habit-update"),
    path("habit/<int:pk>/delete/", HabitDestroyApiView.as_view(), name="habit-delete"),
    path("habit-list/", HabitListView.as_view(), name="habit-list"),
]
