from django.http import HttpResponse


def index(request):
    return HttpResponse('Yes! У меня получилось!')


def second_page(request):
    return HttpResponse('Можно переходить к проекту!')
