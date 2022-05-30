from django.shortcuts import render, redirect, resolve_url
from .models import Book,Comment
from .forms import *
# Create your views here.

def index(request):

    book_list= Book.objects.all()

    response= render(request, 'books/index.html', {'books':book_list})

    request.session["fav_books"] = ["Harry Potter", "Secret Garden"]

    signed_cookie = request.get_signed_cookie("important", None)

    if "fontsize" in request.GET:
        current_font = request.COOKIES['fontsize']
        print("GET:fontsize" +request.COOKIES.get('fontsize'))

    elif "fontsize" in request.POST:
        current_font = request.POST.get('fontsize')
        print("POST:fontsize" +request.POST['fontsize'])

    response.set_signed_cookie("fontsize", 'current_font')

    return response

def add_book(request):

    if request.method == 'POST':
        bookform = BookForm(request.POST, request.Files)

        if bookform.is_valid():
           book = bookform.save()
           return redirect(resolve_url("books:index"))

    form = BookForm()
    return render(request, 'books/add_book.html', {"form": form})

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            added_comment = Comment(name=comment_form.cleaned_data["name"],
                                    comment=comment_form.cleaned_data["content"],book=book)
            added_comment.save()
        else:
            print(comment_form.errors)

    context = {"book": book, "form": CommentForm()}

    return render(request, 'books/book_detail.html', context)



