from pydoc import resolve
from django.http import HttpRequest
from django.shortcuts import render , redirect
from .models import Books , Reviews
from .forms import BooksModelForm , CommentForm

# Create your views here.



def index (request : HttpRequest) :
    if 'favs_only' in request.GET:
        favs_Book = request.session.get("favs", [])
        Books_list = Books.objects.filter(id__in = favs_Book)
    else:
         Books_list = Books.objects.all()
        
    context = {'Books':Books_list , 'display' : True }

    response = render(request , 'index.html' , context)

    if 'font_size' in request.GET:
        response.set_cookie('font_size', request.GET['font_size'])


    return response




def add_Book(request : HttpRequest):



    if request.method == 'POST':
        Bookform= BooksModelForm(request.POST)

        if Bookform.is_valid():
            Bookform.save() 
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


def add_favorite(request:HttpRequest , Book_id):

    request.session['favs'] = request.session.get('favs',[])+ [Book_id]
    print(request.session['favs'])
    return redirect(('index'))
