from django.shortcuts import HttpResponse

def studylog(request, user_slug):
    return HttpResponse(f"Здесь будет лог учёбы для {user_slug}")