from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cars_site(request):
    return HttpResponse("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body style="background-color: skyblue;">
    <h1>Welcome to my Gallery</h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis dolorum minima magnam nisi consequatur! Velit atque suscipit et eaque omnis laboriosam repellat asperiores beatae, fuga qui modi in adipisci quia.</p>
</body>
</html>""")

def show_pride(request):
    return HttpResponse("این پراید محصول ایران است")

def show_tiba(request):
    return HttpResponse("این تیبا محصول ایران است")

def show_rana(request):
    return HttpResponse("این رانا محصول ایران است")