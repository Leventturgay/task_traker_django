from django.http import HttpResponse


def home(request):
    return HttpResponse('Api mize Hoşgeldiniz')
