from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import UserTextbook, UserLesson, CustomUser


def progress_bar(request, user_slug):
    user_id = CustomUser.objects.get(slug=user_slug).id
    user_name = CustomUser.objects.get(slug=user_slug).name
    user_textbooks = UserTextbook.objects.filter(user_id=user_id)
    user_lessons = UserLesson.objects.filter(user_id=user_id)
    data = {
        'title': f'Прогресс: {user_name}',
        'user_name': user_name,
        'user_textbooks': user_textbooks,
        'user_lessons': user_lessons,
    }
    return render(request, 'progress_bar.html', context=data)


def sync_completion_status(request):
    if request.method == 'POST' and request.is_ajax():
        completed_lessons = request.POST.getlist('completed_lessons[]')
        # Update completion status in the database
        UserLesson.objects.filter(id__in=completed_lessons).update(completed=True)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request'})


