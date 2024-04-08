from django.shortcuts import render
from django.http import JsonResponse
from .models import Textbook, Lesson


def progress_bar(request):
    textbooks = Textbook.objects.all()
    return render(request, 'progress_bar.html', {'textbooks': textbooks})


def sync_completion_status(request):
    if request.method == 'POST' and request.is_ajax():
        completed_lessons = request.POST.getlist('completed_lessons[]')
        # Update completion status in the database
        Lesson.objects.filter(id__in=completed_lessons).update(completed=True)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request'})

