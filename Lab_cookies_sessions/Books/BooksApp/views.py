from django.shortcuts import render, redirect, resolve_url
from django.http import HttpRequest, HttpResponse
from .models import Book, Review
from .form import  BookModelForm, CommentForm


def index(request: HttpRequest):
    book_list = Book.objects.all()

    context = {"books": book_list, "display": True}
    response = render(request, 'index.html', context)

    # add session of fav book
    request.session["fav_books"] = ["Harry Potter", "The Secret"]

    # we use signed cookie to protect the cookie from maniulation
    signed_cookie = request.get_signed_cookie("important", None)

    # Using cookies, user can change the font size to small or big (use css to achieve this)
    if "font size" in request.GET:
        # setting a cookie
        # response.set_cookie("font size", "true")
        response.set_signed_cookie("important", "some value")

    return response


def add_book(request: HttpRequest):
    if request.method == 'POST':
        bookModelForm = BookModelForm(request.POST, request.FILES)
        if bookModelForm.is_valid():
            book = bookModelForm.save()
            return redirect(resolve_url("books:index"))

    form = BookModelForm()
    return render(request, 'books.html', {"form": form})


def list_books(request: HttpRequest, book_index):
    if request.GET:
        print(request.GET)

    books = ["Harry Potter", " Animal Farm", " The Secret"]
    print(book_index)
    context = {"books": books[int(book_index)]}
    return render(request, 'index.html', context)