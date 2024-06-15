import csv
import os
import sys

import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "progress_bar_project.settings")
django.setup()

from core.models.progress_bar import Lesson, Textbook

from progress_bar_project.settings import BASE_DIR


def get_textbook(textbook):
    Textbook(name=textbook).save()


def get_lesson(csv_file):
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            textbook_name = row[0]
            try:
                textbook = Textbook.objects.get(name=textbook_name)
            except Textbook.DoesNotExist:
                print(f"Textbook with name '{textbook_name}' does not exist.")
                continue
            Lesson.objects.create(textbook=textbook, name=row[1])


if not os.path.exists("../lesson_data"):
    print("Directory '../lesson_data' does not exist.")

root, _, files = next(os.walk(os.path.join(BASE_DIR, "lesson_data")))
textbooks = [file.rstrip(".csv") for file in files]
print(textbooks)
filepaths = [os.path.join(root, file) for file in files]

for t in textbooks:
    get_textbook(t)

for fp in filepaths:
    get_lesson(fp)
