
from django.shortcuts import render, redirect, resolve_url
from django.http import HttpRequest, HttpResponse
from .models import Books, Comment
from .forms import BooksForm, BooksModelForm, CommentForm


# Create your views here.


def index(request: HttpRequest):
    book_list = Books.objects.all()

    context = {"books": book_list, "display": True}
    response = render(request, 'books/index.html', context)

    request.session["fav_books"] = ["cinderla", "1984"]

    signed_cookie = request.get_signed_cookie("important", None)

    if "dark_mode" in request.GET:
        # setting a cookie
        response.set_signed_cookie("important", "some value")
    return response


def add_books(request: HttpRequest):
    if request.method == 'POST':
        bookModelForm = BooksModelForm(request.POST, request.FILES)

        if bookModelForm.is_valid():
            book = bookModelForm.save()
            return redirect(resolve_url("books:index"))

    form = BooksModelForm()
    return render(request, 'books/add_book.html', {"form": form})


def list_books(request: HttpRequest ):
    if request.GET:
        print(request.GET)
    books = ["1984", "2012", " book2"]
    context = {"book": books[int()]}
    return render(request, 'books/list.html', context)


def book_detail(request: HttpRequest, book_id):
    book = Books.objects.get(pk=book_id)

    session_content = request.session.get("fav_books", None)
    print(session_content)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            added_comment = Comment(book=book, name=comment_form.cleaned_data["name"],
                                    content=comment_form.cleaned_data["content"])
            added_comment.save()
        else:
            print(comment_form.errors)

    context = {"book": book, "form": CommentForm()}

    return render(request, 'books/book_detail.html', context)


# to delete a movie
def delete_book(request: HttpRequest, book_id):
    book = Books.objects.get(pk=book_id)
    book.delete()
