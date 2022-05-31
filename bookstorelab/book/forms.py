from django import forms
from .models import Book, Comment

class BookForm(forms.Form):

    title = forms.CharField(label="Movie Title", max_length=512)
    desc = forms.CharField(label="Movie Desc", widget=forms.widgets.Textarea)

class BookModelForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__' #to include all fields



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__' #to include all fields