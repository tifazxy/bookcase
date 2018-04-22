from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Storage, Comment

class StorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = ['book_name']
        lables = {'book_name': ''}
        #fields = "__all__"
        #fields = ['book_name', 'price'] 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        #~ fields = ['text']
        #~ lables = {'text': ''}
        fields = ['text']
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        #~ help_texts = {
            #~ 'text': _('Some useful help text.'),
        #~ }
