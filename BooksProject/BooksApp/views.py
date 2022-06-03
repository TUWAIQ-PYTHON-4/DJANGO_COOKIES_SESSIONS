from django.shortcuts import render, redirect, resolve_url
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from .models import Books, Comments
from .forms import CommentsModelForm

def Indix(request : HttpRequest):

    if 'favs_only' in request.GET:
        favs_books = request.session.get("favs", [])
        book_list = Books.objects.filter(id__in = favs_books)
    else:
        book_list = Books.objects.all()

    context = {"books": book_list, "display": True, "dark_mode" : False}

    response = render(request, 'Books/index.html', context)

    if 'font_size' in request.GET:
        response.set_cookie('font_size', request.GET['font_size'])


    return response

'''
    books = Books.objects.all()
    context = {'books': books}
    return render(request, "Books/index.html", context)




        if request.method == "POST":
        form = CommentsModelForm(request.POST)
    else:
        form = CommentsModelForm()
    if request.method == "POST":
        form = CommentsModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(resolve_url("favorite"))
    form = CommentsModelForm()
    context = {"form": form}


    def show_comment(request):
    context = {"form": Comments()}

    
    return render(request, "Books/detail.html", context)
'''




def Book_detail(request:HttpRequest, book_id):


    book = Books.objects.get(pk=book_id)

    #get the session data or none
    session_content = request.session.get("fav_books", None)
    print(session_content)

    if request.method == "POST":
        comment_form = CommentsModelForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
        else:
            print(comment_form.errors)
        
    comments = Comments.objects.all()
    context = {"book" : book , 'comments': comments, "form" : CommentsModelForm()}

    return render(request, "Books/detail.html", context)



def add_favorite(request:HttpRequest, book_id):
    
    request.session["favs"] = request.session.get("favs", []) + [book_id]
    print(request.session["favs"])

    return redirect(resolve_url("Books:index"))