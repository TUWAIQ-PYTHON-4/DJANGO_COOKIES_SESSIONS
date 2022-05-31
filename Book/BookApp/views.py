from django.template import response

from django.shortcuts import render, redirect, resolve_url
from .models import AddBooks, AddComment
from .forms import AddBookForm, AddCommentForm


# Create your views here.

def home(request):
    if 'fav_only' in request.GET:
        fav_book = request.session.get("fav", [])
        book_list = AddBooks.objects.filter(id__in=fav_book)
    else:
        book_list = AddBooks.objects.all()
    Comments = AddComment.objects.all()
    Comment = {"movies": book_list,'Comments': Comments}
    response = render(request, 'details.html', Comment)
    return response


def setcookie(request):
    Comments = AddComment.objects.all()
    Comment = {'Comments': Comments}

    font_size = request.GET.get('font_size')
    if font_size == 'big':
        font_size = '40px'

    elif font_size == 'small':
        font_size = '10px'

    else:
        Comment['font_size'] = '16px'

    Comment['font_size'] = font_size

    response = render(request, "index.html", Comment)
    response.set_cookie('font_size', font_size)
    return response


def showBook(request):
    Books = AddBooks.objects.all()
    return render(request, 'showBook.html', {'Books': Books})


def addBook(request):
    if request.method == "POST":
        form = AddBookForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("showBook")
            except:
                pass
    else:
        form = AddBookForm()
    return render(request, 'addBook.html', {'form': form})


def addComment(request, id):
    Books = AddBooks.objects.get(id=id)
    # get the session
    session_content = request.session.get("fav_movies", None)
    print(session_content)
    return render(request, 'details.html', {'Books': Books})


def fav(request, id):
    request.session["fav"] = request.session.get("fav", []) + [id]
    print(request.session["fav"])
    return redirect(resolve_url("addComment"))

    return redirect(resolve_url("details"))


def showComment(request):
    Comments = AddComment.objects.all()
    return render(request, 'index.html', {'Comments': Comments})


def addComment2(request):
    if request.method == "POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('showComment')
            except:
                pass
    else:
        form = AddCommentForm()
    return render(request, 'details.html', {'form': form})
