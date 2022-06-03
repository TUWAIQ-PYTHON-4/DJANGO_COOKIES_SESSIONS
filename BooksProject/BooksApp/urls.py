from django.urls import path
from . import views



urlpatterns = [
    path('', views.Indix, name='index'),
    path('detail/<book_id>', views.Book_detail, name= 'detail'),
    path("add_favorite/<book_id>", views.add_favorite, name="add_favorite"),
] 
