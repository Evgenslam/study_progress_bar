from django.shortcuts import render
from django.http import JsonResponse
from .models import Textbook, Lesson


def progress_bar(request):
    textbooks = Textbook.objects.all()
    return render(request, 'progress_bar.html', {'textbooks': textbooks})


def update_lesson_status(request):
    if request.method == 'POST':
        lesson_id = request.POST.get('lesson_id')
        completed = request.POST.get('completed')

        try:
            lesson = Lesson.objects.get(pk=lesson_id)
            lesson.completed = completed
            lesson.save()
            return JsonResponse({'success': True})
        except Lesson.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Lesson does not exist'})
    else:
        return JsonResponse({'success': False, 'error': 'Only POST requests are allowed'})
