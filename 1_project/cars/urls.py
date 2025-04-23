from django.urls import path
from .views import *

urlpatterns = [
    path("", cars_site),
    path("pride/", show_pride),
    path("tiba/", show_tiba),
    path("rana/", show_rana),
]
