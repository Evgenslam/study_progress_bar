import csv
from progress_bar_app.models import Lesson, Textbook


def import_lessons(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            textbook_name = row[0]
            try:
                textbook = Textbook.objects.get(name=textbook_name)
            except Textbook.DoesNotExist:
                print(f"Textbook with name '{textbook_name}' does not exist.")
                continue
            Lesson.objects.create(textbook=textbook, name=row[1])


if __name__ == "__main__":
    import_lessons('progress_bar_project/lessons.csv')
