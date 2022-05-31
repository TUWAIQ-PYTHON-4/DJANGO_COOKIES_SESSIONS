from django.shortcuts import render , resolve_url , redirect
from django.http import HttpRequest
from .forms import bookModelForm, CommentForm
from .models import Comment, book


def index(request: HttpRequest):
    book_list = book.objects.all()

    context = {"books": book_list, "display": True}
    response = render(request, 'index.html', context)


#    request.session["fav_books"] = ["book1", "book2"]


    signed_cookie = request.get_signed_cookie("important", None)

    if "chang_size" in request.GET:
        response.set_signed_cookie("important", "some value")

    return response


def book_browse(request:HttpRequest, book_id):
    Book = book.objects.get(pk=book_id)

    #get the session data or none
    session_content = request.session.get("fav_movies", None)
    print(session_content)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            added_comment = Comment(book=Book, name=comment_form.cleaned_data["name"], content = comment_form.cleaned_data["content"])
            added_comment.save()
        else:
            print(comment_form.errors)


    context = {"book" : book, "form" : CommentForm()}

    return render(request, 'book_detail.html', context)


def list_books(request : HttpRequest, book_index):

    if request.GET:
        print(request.GET)

    books = ["bbok1", "book2", "book3"]
    print(book_index)
    context = {"movie" : books[int(book_index)]}
    return render(request, 'list.html', context)


def add_books(request : HttpRequest):

    if request.method == 'POST':
        booksModelForm = bookModelForm(request.POST, request.FILES)

        if bookModelForm.is_valid():
            book = booksModelForm.save()
            return redirect(resolve_url("book:index"))

    form = bookModelForm()
    return render(request, 'add_book.html', {"form" : form})

def book_detail(request:HttpRequest, book_id):
    books = book.objects.get(pk=book_id)

    #get the session data or none
    session_content = request.session.get("fav_books", None)
    print(session_content)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            added_comment = Comment(book=books, name=comment_form.cleaned_data["name"], content = comment_form.cleaned_data["content"])
            added_comment.save()
        else:
            print(comment_form.errors)


    context = {"book" : book, "form" : CommentForm()}

    return render(request, 'book_detail.html', context)