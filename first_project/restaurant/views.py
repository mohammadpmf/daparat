from django.shortcuts import render
from django.http import HttpResponse


def show_restaurant(request):
    return HttpResponse("به رستوران خوش آمدید")