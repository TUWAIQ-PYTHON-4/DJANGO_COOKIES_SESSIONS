from django import forms
from .models import Book, Comment

class MovieForm(forms.Form):

    title = forms.CharField(label="Movie Title", max_length=512)
    desc = forms.CharField(label="Movie Desc", widget=forms.widgets.Textarea)
    rating = forms.ChoiceField(choices=[["1", "1 Star"], ["2", "2 Stars"]], widget=forms.widgets.RadioSelect)

class MovieModelForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__' #to include all fields
        #fileds = ['title', 'desc'] #to include specific fields only


class CommentForm(forms.Form):

    name = forms.CharField(max_length=124)
    content  = forms.CharField(widget=forms.widgets.Textarea)