from django.shortcuts import render
from django.http import JsonResponse
from theJunior.models import Birthday


def index(request):
    return render(request, 'theJunior/index.html')


def birthday(request):
    bday = Birthday.objects.all().values()
    birthday_list = list(bday)
    return JsonResponse(birthday_list, safe=False)
# renderto response
