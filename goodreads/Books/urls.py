from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('home', views.index , name='home_index'),
    path('bookForm',views.bookForm, name = 'bookForm'),
    path('bookReviews/<book_id>',views.bookReviews , name = 'bookReviews' ),
    path('add_fav_books/<book_id>', views.add_fav_books, name='add_fav_books'),
    path('disply_fav_books',views.disply_fav_books, name = 'disply_fav_books'),

]