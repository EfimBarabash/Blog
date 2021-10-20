from django import forms
from .models import Post, Comment


class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }


class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


