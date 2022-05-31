from django.shortcuts import render, redirect, resolve_url
from django.http import HttpRequest, HttpResponse
from .models import Book, Comment
from .forms import BookForm, BookModelForm, CommentForm


# Create your views here.


def index(request: HttpRequest):
    Book_list = Book.objects.all()

    context = {"book": Book_list, "display": True}
    response = render(request, 'index.html', context)
    return response




def add_book(request: HttpRequest):
    if request.method == 'POST':
        BookModelForm = BookModelForm(request.POST, request.FILES)

        if BookModelForm.is_valid():
            movie = BookModelForm.save()
            return redirect(resolve_url("index"))

    form = BookModelForm()
    return render(request, 'add_book.html', {"form": form})



def book_detail(request: HttpRequest, book_id):
    movie = Book.objects.get(pk=book_id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            added_comment = Comment(movie=movie, name=comment_form.cleaned_data["name"],
                                    content=comment_form.cleaned_data["content"])
            added_comment.save()
        else:
            print(comment_form.errors)

    context = {"book": book, "form": CommentForm()}

    return render(request, 'book_detail.html', context)


# to delete a book
def delete_book(request: HttpRequest, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()

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