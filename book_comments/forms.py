from django import forms
from .models import ArticleInformation


class ArticleForm(forms.ModelForm):
    class Meta:
        model = ArticleInformation
        fields = ['title', 'text']
        lables = {'title': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        #fields = "__all__"
        #fields = ['book_name', 'price']