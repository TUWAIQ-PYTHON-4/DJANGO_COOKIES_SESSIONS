from django.http import HttpRequest
from django.shortcuts import render, redirect, resolve_url
from .models import *
from .forms import *


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()

    form = BookForm()
    return render(request, 'add_book.html', {"form": form})


def home(request):
    all_books = Book.objects.all()
    context_book = {"all_books": all_books}
    return render(request, 'home.html', context_book)

    if 'font_size' in request.GET:
        response.set_cookie('font_size', request.GET['font_size'])


def add_comment(request: HttpRequest, book_id):
    #book = Book.objects.get(pk=book_id)
    all_books = Book.objects.all()
    context_book = {"all_books": all_books}
    all_comment = Comment.objects.all()
    context_comment = {"all_comment": all_comment}
    return render(request, 'add_comment.html', context_book, context_comment)


def add_fav_book(request: HttpRequest, book_id):
    request.session["favs"] = request.session.get("favs", []) + [book_id]
    print(request.session["favs"])

    return redirect(resolve_url("movies:index"))


