from django.shortcuts import render, redirect
from .models import Books,Review
from .forms import BookModelForm,ReviewForm

def index(request):
    books_list = Books.objects.all()
    context = {'books': books_list,'display':True, 'font_size':False}
    response = render(request, 'index.html', context)

    #adding a session
    #fav_books = request.session["fav_books"]
    #fav_books = [books_list.get]
    
    if "fontsize" in request.COOKIES:
        print("changed to True")
        context['font_size'] = True

    if "fontsize" in request.GET:
        response.set_cookie("fontsize", "true")

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
    #get the session data or none
    #session_content = request.session.get("fav_books", None)
    #print(session_content)

    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            added_comment = Review(book=book, name=review_form.cleaned_data["name"], comment = review_form.cleaned_data["comment"])
            added_comment.save()
        else:
            print(review_form.errors)
    
    context = {"book": book, "form": ReviewForm()}
    return render(request, 'book_detail.html', context)