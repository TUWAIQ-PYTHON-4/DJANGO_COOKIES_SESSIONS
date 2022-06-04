from django.http import HttpRequest
from django.shortcuts import redirect, render, resolve_url
from .forms import Commentform,BookForm
from .models import Book, Comment

# Create your views here.

def index(request : HttpRequest):
    book_list = Book.objects.all()
    favs_books = request.session.get("favs", [])
    favs_books = Book.objects.filter(id__in = favs_books)
    response= render(request,'index.html',{'book':book_list,'favs_books':favs_books})
    if 'font_size' in request.GET:
     response.set_cookie('font_size', request.GET['font_size'])
    return response

    

def addbook(request ):
 if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
 #           return redirect(resolve_url("add"))
 form = BookForm()
 response=  render(request, 'addbook.html', {"form" : form})
 if 'font_size' in request.GET:
  response.set_cookie('font_size', request.GET['font_size'])
 return response



def book(request:HttpRequest,id):
 book = Book.objects.get(pk=id)
 comments=book.comments.all()
 form = Commentform()
 if request.method == 'POST':
    form = Commentform(request.POST, request.FILES)
    if form.is_valid():
      c=form.save(commit=False)
      c.post=book
      c.save()
      form = Commentform() 
 return render(request, 'book.html', {'book' : book, 'form' : form,'comments':comments})




def add_favorite(request:HttpRequest, id):
    
    request.session["favs"] = request.session.get("favs", []) + [id]
    print(request.session["favs"])

    return redirect(resolve_url("index"))


def delete_favorite(request:HttpRequest):
    try:
        del request.session['favs']
    except  KeyError:
        pass
    return redirect(resolve_url("index"))


def browse(request):
    pass

