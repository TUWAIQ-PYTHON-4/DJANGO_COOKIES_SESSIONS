from django.urls import path
from . import views




urlpatterns = [

    path("", views.index, name="index"),
    path("add/", views.add_Book, name="add_Book"),
    path("detail/<Book_id>", views.Book_detail, name="Book_detail")
]
