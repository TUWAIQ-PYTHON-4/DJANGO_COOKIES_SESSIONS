
from django.shortcuts import render,get_object_or_404,redirect,resolve_url
from .models import Book, Comment
from .forms import Commentform,BookForm
from django.http import HttpRequest
# Create your views here.

def listbook(request):
    if 'favs_only' in request.GET:
        favs_book = request.session.get("favs", [])
        book_list = Book.objects.filter(id__in = favs_book)
    else:
        book_list = Book.objects.all()
    context={'book':book_list}
    responses= render(request,'listbook.html',context)
    if 'font_size' in request.GET:
        responses.set_cookie('font_size', request.GET['font_size'])
    return responses

def add(request ):

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            book = form.save()
            return redirect(resolve_url("home"))
    form = BookForm()
    return render(request, 'addbook.html', {"form" : form})

def list_book(request : HttpRequest, book_index):

    if request.GET:
        print(request.GET)

    book = ["Book1", "Book2 ", "Book3"]
    print(book_index)
    context = {"book" : book[int(book_index)]}
    return render(request, 'favo.html', context)


def comment_detile(request, pk):
    post=get_object_or_404(Book, pk=pk)
    if request.method=='POST':
       form= Commentform(request.POST)

       if form.is_valid():
          obj= form.save(commit=False)
          obj.post=post
          obj.save()

          return redirect('post',pk=post.pk)
    else:
        form= Commentform()

    context={
        'post':post,
        'form':form}
    return render(request,'post.html',context)

def add_favorite(request:HttpRequest, book_id):
    request.session["favs"] = request.session.get("favs", [])+ [book_id]
    print(request.session["favs"])
    return redirect(resolve_url("home"))
