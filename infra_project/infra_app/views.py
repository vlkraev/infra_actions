from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось! Можно переходить к проекту!')


def second_page(request):
    return HttpResponse('А это вторая страница! Ну сколько еще ждать?')
