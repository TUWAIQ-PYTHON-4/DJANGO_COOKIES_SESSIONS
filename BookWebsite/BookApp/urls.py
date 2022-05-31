from django.urls import  path
from . import views

urlpatterns = [
    path('',views.listbook,name='home'),
     path("list/<book_index>", views.list_book, name="list_book"),
    path('post/<pk>',views.comment_detile,name='post'),
    path('add/',views.add,name='add'),
    path("add_favorite/<book_id>", views.add_favorite, name="add_favorite")

]