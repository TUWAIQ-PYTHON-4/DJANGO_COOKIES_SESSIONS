from django import forms
from .models import Book,Comment

class BookForm(forms.ModelForm):
    class Meta:
        model= Book
        fields= '__all__'

class Commentform(forms.ModelForm):
    class Meta:
        model=Comment
        fields= ['name', 'content']