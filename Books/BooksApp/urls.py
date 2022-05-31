from django.urls import path
from . import views

name = 'BooksApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_book/', views.add_book, name='add_book'),
    path('books_list/', views.books_list, name='books_list'),
    path('books_info/<book_id>/', views.books_info, name='books_info'),
    path('add_favorite/<book_id>/', views.add_favorite, name='add_favorite'),


]