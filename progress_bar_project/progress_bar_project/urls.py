from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bar/', include('progress_bar_app.urls', namespace='bar')),
    path('users/', include('users.urls', namespace='users'))
]