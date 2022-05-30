from django import forms
from .models import Book, Comment

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'


class CommentForm(forms.Form):

    name = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.widgets.Textarea)