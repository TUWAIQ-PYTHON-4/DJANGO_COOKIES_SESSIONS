from urllib import response

from django.shortcuts import render , resolve_url , redirect
from django.http import HttpRequest
from .forms import bookModelForm, CommentForm
from .models import Comment, book


def add_favorite(request:HttpRequest, book_id):
    request.session["favs"] = request.session.get("favs", [])+ [book_id]
    print(request.session["favs"])
    return redirect(resolve_url("books:index"))

def index(request: HttpRequest):
    book_list = book.objects.all()

    context = {"books": book_list, "display": True}
    response = render(request, 'index.html', context)

    if 'font_size' in request.GET:
        response.set_cookie('font_size', request.GET['font_size'])

    if 'favs_only' in request.GET:
        favorite_book = request.session.get("favs", [])
        book_list = book.objects.filter(id__in=favorite_book)
    else:
        book_list = book.objects.all()

    return response


def book_browse(request:HttpRequest, book_id):
    Book = book.objects.get(pk=book_id)


    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            added_comment = Comment(book=Book, name=comment_form.cleaned_data["name"], content = comment_form.cleaned_data["content"])
            added_comment.save()
        else:
            print(comment_form.errors)


    context = {"book" : book, "form" : CommentForm()}

    return render(request, 'book_detail.html', context)

def cookies(request):
    signed_cookie = request.get_signed_cookie("important", None)

    if "chang_size" in request.GET:
        response.set_signed_cookie("important", "some value")

def list_books(request : HttpRequest, book_index):

    if request.GET:
        print(request.GET)

    books = ["bbok1", "book2", "book3"]
    print(book_index)
    context = {"book" : books[int(book_index)]}
    return render(request, 'list.html', context)


def add_books(request : HttpRequest):

    if request.method == 'POST':
        booksModelForm = bookModelForm(request.POST, request.FILES)

        if bookModelForm.is_valid():
            book = booksModelForm.save()
            return redirect(resolve_url("books:index"))

    form = bookModelForm()
    return render(request, 'books:add_book.html', {"form" : form})

def book_detail(request:HttpRequest, book_id):
    books = book.objects.get(pk=book_id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            added_comment = Comment(book=books, name=comment_form.cleaned_data["name"], content = comment_form.cleaned_data["content"])
            added_comment.save()
        else:
            print(comment_form.errors)


    context = {"Comment" : Comment, "form" : CommentForm()}

    return render(request, 'bppks:book_detail.html', context)