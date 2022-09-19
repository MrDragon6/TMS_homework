from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User

from django.db import models


class Contestant(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='contestant',
    )

    registration_date = models.DateTimeField(default=datetime.now, blank=True)
    points = models.IntegerField(default=0)
    is_admin = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Contestant'
        verbose_name_plural = 'Contestants'

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    contestant = models.OneToOneField(Contestant, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='profile_avatars/',
                                        default='profile_avatars/default_profile_pic.jpg')
    social_link = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return str(self.contestant)

    @staticmethod
    def get_absolute_url():
        return reverse('home')


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='quiz_imgs/', blank=True)
    is_public = models.BooleanField(default=False)
    likes = models.ManyToManyField(Contestant, related_name='quiz_likes', null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now, null=True, blank=True)

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    title = models.TextField()
    image = models.ImageField(upload_to='question_imgs/', blank=True)
    answer_1 = models.CharField(max_length=200)
    answer_2 = models.CharField(max_length=200)
    answer_3 = models.CharField(max_length=200)
    answer_4 = models.CharField(max_length=200)
    right_answer = models.CharField(max_length=200)
    time_limit = models.IntegerField()

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.title


class SubmittedAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chosen_answer = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Submitted Answers'
        verbose_name_plural = 'Submitted Answers'


class QuizCompletion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    contestant = models.ForeignKey(Contestant, related_name='quiz_completions', on_delete=models.CASCADE)
    completion_time = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()

    class Meta:
        verbose_name = 'Quiz Completion'
        verbose_name_plural = 'Quiz Completions'
