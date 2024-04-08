from django.contrib import admin
from django.urls import include, path
from progress_bar_app.views import progress_bar, update_lesson_status

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bar/', include('progress_bar_app.urls', namespace='bar')),
    path('users/', include('users.urls', namespace='users'))
]