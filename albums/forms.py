__author__ = 'user'
from django.forms import ModelForm
from .models  import Comment,Avatar,Album,Photo


class CommentForm (ModelForm):
    class Meta():
        model=Comment
        fields=['comments_text']

class AvatarForm (ModelForm):
    class Meta():
        model=Avatar
        fields=['avatar_user']

class AlbumsForm(ModelForm):
    class Meta():
        model= Album
        fields=['img','title']

class PhotoForm(ModelForm):
    class Meta():
        model=Photo
        fields=['title','img']