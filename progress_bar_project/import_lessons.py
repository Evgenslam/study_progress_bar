import csv
import os
import django

from variables import textbooks_data

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'progress_bar_project.settings')
django.setup()

from progress_bar_app.models import Lesson, Textbook


def get_lessons(csv_file):
    with open(csv_file, 'r', encoding="utf-8") as f:
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


for t in textbooks_data:
    get_lessons(t["csv_path"])
