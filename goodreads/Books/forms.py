from django import forms
from .models import *
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = [ 'name', 'comment']