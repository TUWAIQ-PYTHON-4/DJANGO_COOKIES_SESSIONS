from django import forms
from .models import Books, Comment


class BooksForm(forms.Form):
    title = forms.CharField(label="Movie Title", max_length=512)
    desc = forms.CharField(label="Movie Desc", widget=forms.widgets.Textarea)


class BooksModelForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'


class CommentForm(forms.Form):
    name = forms.CharField(max_length=124)
    content = forms.CharField(widget=forms.widgets.Textarea)
