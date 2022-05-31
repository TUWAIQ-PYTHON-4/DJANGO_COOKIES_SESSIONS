from django import forms
from .models import Book, Review


class BookForm(forms.Form):
    title = forms.CharField(label="Book Title", max_length=512)
    desc = forms.CharField(label="Book Desc", widget=forms.widgets.Textarea)


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class ReviewForm(forms.Form):
    name = forms.CharField(max_length=50)
    comment = forms.CharField(widget=forms.widgets.Textarea)
