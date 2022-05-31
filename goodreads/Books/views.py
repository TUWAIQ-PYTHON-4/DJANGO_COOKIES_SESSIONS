from django.shortcuts import render,redirect,resolve_url
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from django.http import HttpRequest, HttpResponse

fav_book_set = set()

def index(request):
 books = Book.objects.all()
 context ={'books': books}
 return render(request, 'index.html', context)

def bookForm(request):
 form = BookForm()

 if request.method == 'POST':
    form = BookForm(request.POST)

 if form.is_valid():
    book = Book.objects.create(title = request.POST['title'], description = request.POST['description'])
    return redirect(resolve_url('index'))

 context = {'form': form}
 return render(request, 'book_form.html', context)

def bookReviews(request, book_id):

    book_info = Book.objects.get(id=book_id)
    commints = Reviews.objects.filter(book = book_info)

    form = ReviewsForm()
    if request.method == 'POST':
        form = ReviewsForm(request.POST)

    if form.is_valid():
        Review = Reviews.objects.create(book=book_info ,name = request.POST['name'], comment = request.POST['comment'] )
        return redirect(resolve_url('index'))

    context = {'commints': commints, 'form': form, 'book_info': book_info, 'book_id': book_id}
    return render(request, 'reviews.html', context)

def add_fav_books(request, book_id):
     request.session["fav_books"] = book_id
     fav_book_set.add(request.session.get("fav_books"))
     return redirect(resolve_url('index'))

def disply_fav_books(request):
    list_fav_book = [Book.objects.get(id = i) for i in fav_book_set]
    context = {'list_fav_book': list_fav_book}
    return render(request, 'fav_books.html', context)










