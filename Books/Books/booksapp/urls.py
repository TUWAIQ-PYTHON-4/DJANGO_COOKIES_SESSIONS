from django.urls import path
from . import views

#add namespace for the app
app_name = "booksapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("list/<book_index>", views.list_books, name="list_books"),
    path("add/", views.add_book, name="add_book"),

]