from django import forms
from .models import Posts
from django.contrib.auth import get_user_model

# Form to input the blog post
class PostForm(forms.ModelForm):
    content= forms.CharField(label=None ,widget= forms.Textarea(attrs={'class': 'content-box form-control', 'placeholder': 'Write a post..'}))
    title= forms.CharField(label= None, widget=forms.TextInput(attrs={'class': 'title-box form-control', 'placeholder': 'Enter the title'}))
    class Meta:
        model= Posts
        fields= ('title', 'content',)

