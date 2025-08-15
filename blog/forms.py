from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on blog posts.
    """
    class Meta:
        """
        Specify the django model and order of the fields.
        """
        model = Comment
        fields = ('body',)
