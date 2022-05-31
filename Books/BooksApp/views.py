from django.shortcuts import render, redirect, resolve_url
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from .models import Books, Comments
from .forms import BooksForm, CommentsForm


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
    if 'fav_only' in request.GET:
        fav_books = request.session.get("fav_books", [])
        books_list = Books.objects.filter(id__in=fav_books)
    else:
        books_list = Books.objects.all()

    context = {"books_list": books_list, "display": True, "dark_mode": False}
    response = render(request, 'index.html', context)

    if 'font_size' in request.GET:
        response.set_cookie('font_size', request.GET['font_size'])

    return response


def books_list(request: HttpRequest):
    book_list = Books.objects.all()
    context = {
        'book_list': book_list,
    }
    return render(request, 'books_list.html', context)


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
    context = {"book": book, "form": CommentsForm()}
    return render(request, 'books_info.html', context)


def add_favorite(request: HttpRequest, book_id: int):
    request.session['favs'] = request.session.get('favs', []) + [book_id]
    return redirect(resolve_url('index'))
