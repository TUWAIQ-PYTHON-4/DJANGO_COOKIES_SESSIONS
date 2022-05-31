from django.shortcuts import render, redirect, resolve_url
from django.http import HttpRequest, HttpResponse
from .models import Books, Comment
from .form import CommentForm

def index(request: HttpRequest):
    book_list = Books.objects.all()

    context = {"books": book_list, "display": True}
    response = render(request, 'books/index.html', context)

    request.session["fav_books"] = ["cinderla", "1984"]

    signed_cookie = request.get_signed_cookie("important", None)

    if "fontsize" in request.GET:
        # setting a cookie
        response.set_signed_cookie("important", 'style/main.css')
    return response


def add_books(request):
    context = Books.objects.all()
    return render(request, 'books/index.html', {"context": context})