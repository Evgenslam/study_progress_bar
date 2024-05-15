from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bar/', include('progress_bar_app.urls', namespace='bar')),
    path('studylog/', include('studylog.urls', namespace='studylog')),
    path('users/', include('users.urls', namespace='users'))
]