from django import forms
from .models import Post, Category, User

choices = Category.objects.all().values_list('name', 'name')
choice_list = [choice for choice in choices]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'text', 'snippet', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insert Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'id_value', 'type': 'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Insert Text'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Insert Snippet'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insert Title'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Insert Text'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Insert Snippet'}),
        }


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
