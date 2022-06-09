from django.shortcuts import render, redirect
from .models import Books,Review
from .forms import BookModelForm,ReviewForm

def index(request):
    
    if 'favorites' in request.GET:
        favs_book = request.session.get("favorites", [])
        books_list = Books.objects.filter(id__in = favs_book)
    else:
        books_list = Books.objects.all()


    context = {'books': books_list,'display':True, 'font_size':False}
    response = render(request, 'index.html', context)

    #Cookies
    if 'font_size' in request.GET:
        response.set_cookie('fontsize', request.GET['font_size'])

    if 'favorites' in request.GET:
        favs_book = request.session.get("favorites", [])
        books_list = Books.objects.filter(id__in = favs_book)
    else:
        books_list = Books.objects.all()
    
    return response

    



def add_book(request):

    if request.method == "POST":
        bookModelForm = BookModelForm(request.POST, request.FILES)

        if bookModelForm.is_valid():
            bookModelForm.save()
            return redirect('index')
    
    form = BookModelForm()
    return render(request, 'add_book.html.',{"form":form})

def book_detail(request,book_id):

    book = Books.objects.get(pk=book_id)

    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            added_comment = Review(book=book, name=review_form.cleaned_data["name"], comment = review_form.cleaned_data["comment"])
            added_comment.save()
        else:
            print(review_form.errors)
    
    context = {"book": book, "form": ReviewForm()}
    return render(request, 'book_detail.html', context)

def add_favorite(request, book_id):
    request.session["favorites"] = request.session.get("favorites",[]) + [book_id]
    return redirect('index')
