from django.shortcuts import render, redirect, resolve_url
from django.http import HttpRequest, HttpResponse
from .models import Book, Comment
from .forms import BookForm, BookModelForm, CommentForm
# Create your views here.


def index(request : HttpRequest):

    book_list = Book.objects.all()

    context = {"books": book_list, "display": True}
    response = render(request, 'index.html', context)


    #adding a session
    request.session["fav_books"] = ["Rich Dad Poor Dad"] 


    
    if "bigger_size" in request.GET:
        #setting a cookie
        response.set_cookie("bigger_size", "true")

    return response


def add_book(request : HttpRequest):

    if request.method == 'POST':
        bookModelForm = BookModelForm(request.POST, request.FILES)

        if bookModelForm.is_valid():
            book = bookModelForm.save() 
            return redirect(resolve_url("book:index")) 

    form = BookModelForm()
    return render(request, 'add_book.html', {"form" : form})


def book_detail(request:HttpRequest, book_id):
    book = Book.objects.get(pk=book_id)

    #get the session data or none
    session_content = request.session.get("fav_book", None)
    print(session_content)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            added_comment = Comment(book=book, name=comment_form.cleaned_data["name"], content = comment_form.cleaned_data["content"])
            added_comment.save()
        else:
            print(comment_form.errors)


    context = {"book" : book, "form" : CommentForm()}

    return render(request, 'book_details.html', context)
