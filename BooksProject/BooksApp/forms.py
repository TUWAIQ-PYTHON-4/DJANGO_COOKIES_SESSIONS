from django import forms
from .models import  Books, Comments


class CommentsModelForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = '__all__'   
     