from django.urls import path
from django.views import View
from . import views




urlpatterns = [

    path("", views.index, name="index"),
    path("add/", views.add_Book, name="add_Book"),
    path("detail/<Book_id>", views.Book_detail, name="Book_detail"),
    path("add_favorite/<Book_id>", views.add_favorite , name="add_favorite")
]
