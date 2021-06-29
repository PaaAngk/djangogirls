from django import forms
from .models import Сomments
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class СommentsForm(forms.ModelForm):

    class Meta:
        model = Сomments
        fields = ('author', 'text',)
