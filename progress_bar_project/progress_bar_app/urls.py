from django.contrib import admin
from django.urls import include, path
from progress_bar_app import views

app_name = 'bar'

urlpatterns = [ 
    path('', views.progress_bar, name='progress_bar'),
    path('sync_completion_status/', views.sync_completion_status, name='sync_completion_status')
    ]


