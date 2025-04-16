from django.shortcuts import render
from django.http import HttpResponse

def show_toys(request):
    return HttpResponse("به قسمت اسباب بازی ها خوش آمدید")