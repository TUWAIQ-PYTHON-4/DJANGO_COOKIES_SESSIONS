from django.shortcuts import render, redirect, resolve_url
from django.http import HttpRequest, HttpResponse
from .models import Book
from .forms import BookForm
# Create your views here.


def index(request : HttpRequest):

    movie_list = Book.objects.all()

    context = {"books": list_books, "display": True}

    return render(request, 'Books/index.html', context)



def add_book(request : HttpRequest):

    #movie = Movie(title="A Random Movie", desc="Some Random Desc", rating=4)
    #movie.save()

    if request.method == 'POST':
        book = Book(title=request.POST.get("title"), desc=request.POST.get("desc"), rating=request.POST.get("rating"))
        book.save()
        return redirect(resolve_url("Books:index"))

    form = BookForm()
    return render(request, 'Books/add_book.html', {"form" : form})

def list_books(request : HttpRequest, book_index):

    if request.GET:
        print(request.GET)

    books = ["Titanic", "Monsters Inc.", "Toy Story"]
    print(book_index)
    context = {"book" : books[int(book_index)]}
    return render(request, 'Books/list.html', context)
