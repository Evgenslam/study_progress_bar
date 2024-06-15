import os
import sys

import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "progress_bar_project.settings")
django.setup()

from core.models.progress_bar import CustomUser

students = ["Юлия", "Андрей", "Маргарита", "Антонина"]

[CustomUser.objects.create(name=student) for student in students]
