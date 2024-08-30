from django import forms
from .models import Blog



class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']

class UpdateBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body']