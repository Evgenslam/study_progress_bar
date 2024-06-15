from django.urls import path

from core import views

app_name = "bar"

urlpatterns = [
    path("lessons/<slug:user_slug>", views.lessons_bar, name="lessons_bar"),
    path("seminars/", views.seminars_bar, name="seminars_bar"),
    path("sync_completion_status/", views.sync_completion_status, name="sync_completion_status"),
]
