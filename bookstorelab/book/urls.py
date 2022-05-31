from django.urls import path
from . import views

#add namespace for the app
app_name = "movies"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_book, name="add_movie"),
    path("detail/<book_id>", views.book_detail, name="movie_detail"),
]