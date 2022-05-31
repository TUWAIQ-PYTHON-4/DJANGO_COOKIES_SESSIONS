from django.template import response

from django.shortcuts import render, redirect
from .models import AddBooks, AddComment
from .forms import AddBookForm, AddCommentForm


# Create your views here.

def home(request):
    Comments = AddComment.objects.all()
    Comment = {'Comments': Comments}
    return render(request, 'index.html',Comment )

def setcookie(request):
    Comments = AddComment.objects.all()
    Comment = {'Comments': Comments}

    font_size = request.GET.get('font_size')
    if font_size == 'big':
        font_size = '40px'
        print("ghdgfhgefg")

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
    return render(request, 'details.html', {'Books': Books})


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
