from django.urls import path

from . import views


urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("detail/<int:pk>/", views.Detail.as_view(), name="detail"),
    path("detail/<int:pk>/order/", views.FoodOrder.as_view(), name="order"),
    path("breakfast/", views.Breakfast.as_view(), name="breakfast"),
    path("lunch/", views.Lunch.as_view(), name="lunch"),
    path("dinner/", views.Dinner.as_view(), name="dinner"),
    path("fast-food/", views.FastFood.as_view(), name="fast_food"),
    path("persian/", views.Persian.as_view(), name="persian"),
    path("drinks/", views.Drink.as_view(), name="drinks"),
    path("about-us/", views.AboutUs.as_view(), name="about_us"),
    path("contact-us/", views.contact_us, name="contact_us"),
]
