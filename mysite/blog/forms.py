from django import forms
from django.forms import ModelForm
from blog.models import Post

class PostForm (forms.ModelForm) :
    class Meta:    
        model = Post
        fields = "__all__"