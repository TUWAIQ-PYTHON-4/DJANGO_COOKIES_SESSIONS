from django.urls import path
from . import views

app_name= 'books'

urlpatterns = [
    path("", views.index, name="index"),
    path("add_book/", views.add_book, name="add_book"),
    path("detail/<book_id>", views.book_detail, name="book_detail"),
    path("change_size/", views.change_size, name="change_size"),
    path("fav_book/<book_id>", views.fav_book, name="fav_book")
]