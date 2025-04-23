from django.urls import path
from . import views

urlpatterns = [
    path("ali/", views.ali),
    path("reza/", views.reza),
    path("mohammad/", views.m),
]
