from django import forms
from .models import Books ,Comments


class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = "__all__"


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = "__all__" 
