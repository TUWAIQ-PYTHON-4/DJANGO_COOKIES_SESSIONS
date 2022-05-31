from django.shortcuts import render,  redirect, resolve_url
from django.http import HttpRequest,HttpResponse
from .models import Book, Comment
from .forms import BoookModelForm,CommentForm




def index(requset : HttpRequest):

    book_list =Book.objects.all()
    context = {"books": book_list,"display":True}
    return render(requset, 'index.html',context)


def add_book(request : HttpRequest):

    if request.method == 'POST':
        bookModelForm = BoookModelForm(request.POST, request.FILES)

        if bookModelForm.is_valid():
            book = bookModelForm.save()
            return redirect(resolve_url("index"))

    form = BoookModelForm()
    return render(request, 'add_book.html', {"form" : form})


def list_books(request: HttpRequest, book_index):

    if request.GET:
        print(request.GET)

    books = ["IT book", "Ethical Hacker", "Network Defender"]
    print(book_index)
    context = {"movie": books[int(book_index)]}
    return render(request, 'list.html', context)






def book_detail(request: HttpRequest, book_id):
    book = Book.objects.get(pk=book_id)

    # get the session data or none
    session_content = request.session.get("fav_books", None)
    print(session_content)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            added_comment = Comment(book=book, name=comment_form.cleaned_data["name"],
                                    content=comment_form.cleaned_data["content"])
            added_comment.save()
        else:
            print(comment_form.errors)

    context = {"book": book, "form": CommentForm()}

    return render(request, 'book_detail.html', context)

