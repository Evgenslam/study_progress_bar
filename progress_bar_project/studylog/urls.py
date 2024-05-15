from django.urls import path
from studylog import views

app_name = 'bar'

urlpatterns = [ 
    path('<slug:user_slug>/', views.studylog, name='studylog'),
    ]


