from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_restaurant),
    path("drinks/", views.show_drinks),
    path("fast-food/", views.show_fast_food),
    path("lunch/", views.show_lunch),
    path("about-us/", views.show_about_us),
    path("breakfast/", views.show_breakfast),
    path("lunch/", views.show_lunch),
    path("contact-us-sent/", views.show_contact_us_sent),
    path("contact-us/", views.show_contact_us),
    path("detail/", views.show_detail),
    path("dinner/", views.show_dinner),
    path("order-successful/", views.show_order_successful),
    path("order/", views.show_order),
    path("persian/", views.show_persian),
]
