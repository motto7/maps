from django import forms
from plan.models import Post, Transit, Comment
from project.widgets import PointWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'lnglat','image']

        widgets = {
            'lnglat': PointWidget,
        }


class TransitForm(forms.ModelForm):
    class Meta:
        model = Transit
        fields = ['title', 'cost']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
