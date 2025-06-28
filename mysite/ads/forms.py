from django import forms
from ads.models import Ad, Comment

class CreateForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = "2 MB"

    picture = forms.FileField(required=False, label='Picture to Upload')
    upload_field_name = 'picture'

    class Meta:
        model = Ad
        fields = ['title', 'price', 'text', 'tags', 'picture']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
