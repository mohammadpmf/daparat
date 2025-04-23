from django.shortcuts import render, HttpResponse

def ali(request):
    return HttpResponse("به غذاخوری علی خوش آمدی")


def reza(request):
    return HttpResponse("welcome to reza restaurant")


def m(request):
    return HttpResponse(
        """
<img src="https://www.gfxdownload.ir/uploads/posts/2023-08/iranian-food7.jpg" alt="a picture">
"""
    )