from django import forms
from .models import Book,Review

class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class ReviewForm(forms.Form):
    name = forms.CharField(max_length=124)
    comment  = forms.CharField(widget=forms.widgets.Textarea)