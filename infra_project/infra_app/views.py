from django.http import HttpResponse


def index(request):
    return HttpResponse('Yes! Можно переходить к проекту!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
