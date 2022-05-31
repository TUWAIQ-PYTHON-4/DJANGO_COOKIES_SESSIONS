from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('showBook/', views.showBook, name='showBook'),
    path('addBook/', views.addBook, name='addBook'),
    path('addComment/<int:id>', views.addComment, name='addComment'),
    path('addComment2', views.addComment2, name='addComment2'),
    path('showComment', views.showComment, name='showComment'),
    path('setcookie/',views.setcookie),

]
