from django.shortcuts import render
from django.http import JsonResponse
from .models import Textbook, Lesson


def progress_bar(request):
    textbooks = Textbook.objects.all()
    return render(request, 'progress_bar.html', {'textbooks': textbooks})


def update_lesson_status(request):
    if request.method == 'POST' and request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        lesson_id = request.POST.get('lesson_id')
        completed = request.POST.get('completed') == 'true'  # Convert string to boolean

        # Update lesson status in the database
        lesson = Lesson.objects.get(id=lesson_id)
        lesson.completed = completed
        lesson.save()

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request'})

