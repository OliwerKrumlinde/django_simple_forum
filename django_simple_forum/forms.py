from .models import Post, Thread
from django.forms import ModelForm, forms
from ckeditor.fields import RichTextField


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('created_date', 'thread', 'user', 'up_votes')


class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        exclude = ('section', 'views', 'disabled', 'created_date', 'owner')
