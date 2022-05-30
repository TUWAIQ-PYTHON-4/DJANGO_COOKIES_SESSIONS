from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("comment/<book_id>", views.comment, name="comment"),
    path('setcookie', views.setcookie),
    path("favorites/", views.favorites, name="favorites-list"),
    path("favorites_book/<book_id>", views.favorites_book, name="favorites-detail"),
]