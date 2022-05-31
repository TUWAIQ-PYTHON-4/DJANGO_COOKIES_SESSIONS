from django import forms
from .models import Book, Comment
#from django.utils.timezone import now


class BookForm(forms.Form):

    title = forms.CharField(label="Book Title", max_length=512)
    desc = forms.CharField(label="Book Desc", widget=forms.widgets.Textarea)

class BookModelForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__' #to include all fields
        

class CommentForm(forms.Form):

    name = forms.CharField(max_length=124)
    content  = forms.CharField(widget=forms.widgets.Textarea)
    #date = forms.DateField()
