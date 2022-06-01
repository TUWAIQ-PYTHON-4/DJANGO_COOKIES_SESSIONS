from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "bookapp"

urlpatterns = [
    path('', views.home, name='home'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_comment/<book_id>', views.add_comment, name='add_comment'),
    path('add_fav_book/<book_id>', views.add_fav_book, name='add_fav_book'),

]
