from django.shortcuts import render, resolve_url, redirect
from django.template import response

from .models import Book, Comment
from .forms import BookForm, CommentForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = BookForm(request.POST or None)
        if form.is_valid():
            form.save()
            book_list = Book.objects.all()
            print()
            context = {"books": book_list}
            return render(request, 'index.html', context)
    else:
        book_list = Book.objects.all()
        font_size = request.COOKIES.get("font_size", "15px")
        context = {"books": book_list, "font_size": font_size}
        return render(request, 'index.html', context)






def add(request ):

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            book = form.save()
            return redirect(resolve_url("books:index"))


    form = BookForm()
    return render(request, 'add.html', {"form" : form})

def comment(request , book_id):

    book = Book.objects.get(pk=book_id)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            added_comment = Comment(book=book, name=comment_form.cleaned_data["name"],content=comment_form.cleaned_data["content"])
            added_comment.save()
        else:
            print(comment_form.errors)

    context = {"book": book, "form": CommentForm()}
    return render(request, 'comment.html', context)

def setcookie(request):
        book_list = Book.objects.all()
        context = {"books": book_list}
        font_size = request.GET.get("font_size")
        if font_size.lower() == "big":
            font_size = "30px"
        elif font_size.lower() == "small":
            font_size = "15px"
        else:
            font_size = "25px"

        context["font_size"] = font_size
        response = render(request, 'index.html', context)
        response.set_cookie('font_size', font_size)
        return response

def favorites_book(request,book_id):

    book = Book.objects.get(pk=book_id)
    if not 'fav_books' in request.session or not request.session['fav_books']:
        request.session['fav_books'] =[book.id]
    else:
         saved_list = request.session['fav_books']
         print(saved_list)
         saved_list.append(book.id)
         request.session['fav_books'] = saved_list

    return render(request, 'favorites.html')

def favorites(request):
    session_books = request.session.get("fav_books", [])
    favorite_books = []
    for book_id in session_books:
        book = Book.objects.filter(id=book_id)
        if book.exists():
            favorite_books.append(book.first())
    print(favorite_books)
    context = {"books": favorite_books}
    return render(request, "favoriteslist.html", context)