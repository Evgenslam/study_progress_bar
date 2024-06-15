import os
import django
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "progress_bar_project.settings")
django.setup()

from core.models.progress_bar import CustomUser, Lesson, Textbook, UserLesson, UserTextbook


def populate_user_textbooks():
    textbooks = Textbook.objects.all()
    users = CustomUser.objects.all()

    for user in users:
        for textbook in textbooks:
            UserTextbook.objects.create(user=user, textbook=textbook, completed=False)


def populate_user_lessons():
    lessons = Lesson.objects.all()
    users = CustomUser.objects.all()

    for user in users:
        for lesson in lessons:
            UserLesson.objects.create(user=user, lesson=lesson, completed=False)


populate_user_textbooks()
populate_user_lessons()
