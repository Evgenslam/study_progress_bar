import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'progress_bar_project.settings')
django.setup()

from progress_bar_app.models import Lesson, Textbook


def get_textbook(textbook):
    Textbook(name=textbook).save()


def get_lesson(csv_file):
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


root, _, files = next(os.walk('./lesson_data'))
textbooks = [file.rstrip('.csv') for file in files]
filepaths = [os.path.join(root, file) for file in files]

for t in textbooks:
    get_textbook(t)

for fp in filepaths:
    get_lesson(fp)
