from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from .models import Books, Comments
from .forms import BooksForm, CommentsForm


# Create your views here.


def add_book(request: HttpRequest):
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = BooksForm
    return render(request, 'add_book.html', {'form': form})


def index(request: HttpRequest):
    book_list = Books.objects.all()
    context = {"book_list": book_list, "display": True}
    response = render(request, 'index.html', context)
    request.session["fav_books"] = ["book1", "book2"]
    signed_cookie = request.get_signed_cookie("important", None)
    return response


def books_list(request: HttpRequest):
    return render(request, 'books_list.html', {'book_list':  Books.objects.all(),})


def books_info(request: HttpRequest, book_id: int):
    book = Books.objects.get(pk=book_id)
    session_content = request.session.get("fav_books", None)
    print(session_content)
    if request.method == "POST":
        comment_form = CommentsForm(request.POST)
        if comment_form.is_valid():
            added_comment = Comments(book=book, name=comment_form.cleaned_data["name"],
                                     comment=comment_form.cleaned_data["comment"])
            added_comment.save()
        else:
            print(comment_form.errors)
