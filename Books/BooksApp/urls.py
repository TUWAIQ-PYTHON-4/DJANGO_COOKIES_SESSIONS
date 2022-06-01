from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("list/", views.list_books, name="list_books"),
    path("add/", views.add_books, name="add_books"),
    path("detail/<book_id>", views.book_detail, name="book_detail"),
    path("add_favorite/<book_id>", views.add_favorite, name="add_favorite")
]