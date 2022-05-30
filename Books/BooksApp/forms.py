from django import forms
from .models import Books,Review

class BookModelForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

class ReviewForm(forms.Form):
    name = forms.CharField(max_length=124)
    comment  = forms.CharField(widget=forms.widgets.Textarea)