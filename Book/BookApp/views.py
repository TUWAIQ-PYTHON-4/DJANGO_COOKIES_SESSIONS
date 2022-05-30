from django.shortcuts import render, redirect
from .models import AddBooks , AddComment
from .forms import AddBookForm, AddCommentForm


# Create your views here.

def home(request):
    return render(request, 'index.html')


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

def showComment(request):
    Comments = AddComment.objects.all()
    return render(request, 'index.html', {'Comments': Comments})
