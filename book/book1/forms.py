from .models import book
from django import forms

class bookModelForm(forms.ModelForm):

    class Meta:
        model = book
        fields = '__all__'

class CommentForm(forms.Form):

    name = forms.CharField(max_length=124)
    content  = forms.CharField(widget=forms.widgets.Textarea)