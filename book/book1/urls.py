from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.index, name="index"),
    path("list/<book_index>", views.list_books, name="list_movies"),
    path("add/", views.add_books, name="add_book"),
    path("detail/<book_id>", views.book_detail, name="book_detail"),
    path("add_favorite/<book_id>", views.add_favorite, name="add_favorite")

]