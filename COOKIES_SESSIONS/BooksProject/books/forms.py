from django import forms
from .models import Book


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class CommentForm(forms.Form):
    name = forms.CharField(max_length=124)
    content = forms.CharField(widget=forms.widgets.Textarea)
