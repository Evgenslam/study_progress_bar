from django.contrib import admin
from django.urls import path
from progress_bar_app.views import progress_bar, update_lesson_status

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', progress_bar, name='progress_bar'),
    path('update_lesson_status/', update_lesson_status, name='update_lesson_status'),
]