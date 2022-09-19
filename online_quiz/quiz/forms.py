from django import forms
from .models import User, Quiz, Question


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class QuestionAddForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('quiz', 'title', 'image', 'answer_1', 'answer_2', 'answer_3', 'answer_4',
                  'right_answer', 'time_limit')
        widgets = {'quiz': forms.HiddenInput()}


class QuizAddForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('title', 'description', 'image', 'is_public', 'likes', 'created_at')
        widgets = {'is_public': forms.HiddenInput(),
                   'likes': forms.HiddenInput(),
                   'created_at': forms.HiddenInput()}
