from django.urls import path
from . import views

#add namespace for the app
app_name = "books"

urlpatterns = [
   path("", views.index, name="index"),
   
]