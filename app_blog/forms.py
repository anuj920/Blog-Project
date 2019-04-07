from django import forms
from app_blog.models import Post,Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('title','text')

        widgets = {
            'title': forms.TextInput(attrs = {'class': 'textinputclass'}),
            'text' : forms.Textarea(attrs = {'class': 'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author': forms.TextInput(attrs = {'class': 'textinputclass'}),
            'text' : forms.Textarea(attrs = {'class': 'editable medium-editor-textarea'})
        }
class CommentAddForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('text',)

        widgets = {
            'text' : forms.Textarea(attrs = {'class': 'editable medium-editor-textarea'})
        }