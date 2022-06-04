from django.urls import path
from . import views

#add namespace for the app

urlpatterns = [
    path('', views.index, name="index"),
    path('addbook/', views.addbook, name="addbook"),
    path('book/<id>', views.book, name="book"),
    path('add_favorite/<id>', views.add_favorite, name="add_favorite"),
    path('delete_favorite/', views.delete_favorite, name="delete_favorite"),




]