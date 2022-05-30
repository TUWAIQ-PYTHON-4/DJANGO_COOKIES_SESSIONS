from django import forms
from .models import AddBooks, AddComment


class AddBookForm(forms.ModelForm):
    class Meta:
        model = AddBooks
        fields = '__all__'


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = AddComment
        fields = '__all__'
