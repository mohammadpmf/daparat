from django.urls import path
from . import views

urlpatterns = [
    path("cars/car1", views.car1),
    path("cars/car2", views.car2),
    path("cars/car3", views.car3),
    path("lego/", views.lego),
]
