from django import forms
from .models import Books


class BooksModelForm(forms.ModelForm):
    class Meta :
        model = Books
        fields = '__all__'




class CommentForm(forms.Form):

    name = forms.CharField(max_length=124)
    content  = forms.CharField(widget=forms.widgets.Textarea)