from django import forms
from .models import Сomments
from .models import Post
from .models import SubСomments


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class СommentsForm(forms.ModelForm):

    class Meta:
        model = Сomments
        fields = ('author', 'text',)


class SubСommentsForm(forms.ModelForm):

    class Meta:
        model = SubСomments
        fields = ('author', 'text',)
        