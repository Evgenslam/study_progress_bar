from django.contrib import admin

from .models import CustomUser, Lesson, Seminar, UserLesson, UserTextbook

admin.site.register(
    [
        CustomUser,
        Lesson,
        UserLesson,
        UserTextbook,
    ]
)
