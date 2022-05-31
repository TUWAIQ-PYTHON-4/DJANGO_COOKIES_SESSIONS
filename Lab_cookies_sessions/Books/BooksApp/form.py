from django import forms
from .models import Books


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

class CommentForm(forms.Form):

    name = forms.CharField(max_length=50)
    comment = forms.CharField(widget=forms.widgets.Textarea)


