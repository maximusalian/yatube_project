from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def group_posts(request):
    return HttpResponse(f'Группа {any_slug}')
