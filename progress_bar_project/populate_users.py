import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'progress_bar_project.settings')
django.setup()

from progress_bar_app.models import CustomUser


students = ['Юлия', 'Андрей', 'Наиль', 'Антонина']

[CustomUser.objects.create(name=student) for student in students]


