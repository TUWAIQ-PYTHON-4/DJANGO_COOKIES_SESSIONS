from django.shortcuts import render, redirect, resolve_url
from .models import Book,Comment
from .forms import *
# Create your views here.


def fav_book(request, book_id):
    fav_book = Book.objects.get(pk=book_id)
    save_book = request.session['fav_books']

    if fav_book not in request.session['fav_books']:
        request.session['fav_books'] = [book_id]
        list_saved= Book.objects.get(id=book_id)
        save_book.append(list_saved)

    response = render(request, 'books/fav_book.html', {'fav_book': save_book})
    return response


def change_size(request):
    font_size = request.GET.get('font_size')
    if font_size == 'big':
        font_size = '40px'
    elif font_size == 'small':
        font_size == '16px'
    else:
        font_size == '23px'

    response = render(request, 'books/index.html', {'font_size': font_size})
    response.set_signed_cookie("font_size", 'font_size')
    return response

def index(request):

    book_list= Book.objects.all()
    font_size = request.COOKIES.get('font_size', '16px')
    response= render(request, 'books/index.html', {'books':book_list, 'font_size': font_size})

    return response

def add_book(request):

    if request.method == 'POST':
        bookform = BookForm(request.POST)

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



