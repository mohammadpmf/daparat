from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("add/", views.add),
    path("detail/<int:pk>/", views.detail),
]
