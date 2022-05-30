from django.http import HttpRequest
from django.shortcuts import render , redirect
from .models import Books , Reviews
from .forms import BooksModelForm , CommentForm

# Create your views here.



def index (request : HttpRequest) :
    Books_list = Books.objects.all()
    context = {'Books':Books_list , 'display' : True }
    return render(request , 'index.html' , context)



def add_Book(request : HttpRequest):

    if request.method == 'POST':
        movieModelForm = BooksModelForm(request.POST)

        if movieModelForm.is_valid():
            Book = BooksModelForm.save() 
            return redirect('index') 

    form = BooksModelForm()
    return render(request, 'add_Books.html', {"form" : form})


def Book_detail(request:HttpRequest, Book_id):
    Book = Books.objects.get(pk=Book_id)

    # get the session data or none
    # session_content = request.session.get("fav_movies", None)
    # print(session_content)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            added_comment = Reviews(book=Book, name=comment_form.cleaned_data["name"], content = comment_form.cleaned_data["content"])
            added_comment.save()
        else:
            print(comment_form.errors)


    context = {"Book" : Book, "form" : CommentForm()}

    return render(request, 'Book_detail.html', context)
