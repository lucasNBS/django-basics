from django import forms
from .models import Post

class PostForm(forms.ModelForm):

  class Meta:
    model = Post
    fields = '__all__'
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-input'}),
      'description': forms.TextInput(attrs={'class': 'form-input'}),
      'content': forms.Textarea(attrs={'class': 'form-textarea'}),
    }