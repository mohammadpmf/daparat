from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add, name="add"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("recent_posts/", views.recent_posts, name="recent_posts"),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path("update/<int:pk>/", views.update, name="update"),
]
