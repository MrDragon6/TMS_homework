from django import forms
from .models import Post, Category, User, Comment, Profile

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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_picture', 'website_url',
                  'facebook_url', 'vkontakte_url', 'instagram_url')

        widgets = {
                'bio': forms.Textarea(attrs={'class': 'form-control'}),
                'profile_picture': forms.TextInput(attrs={'class': 'form-control'}),
                'website_url': forms.TextInput(attrs={'class': 'form-control'}),
                'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
                'vkontakte_url': forms.TextInput(attrs={'class': 'form-control'}),
                'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            }
