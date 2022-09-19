from django.contrib import admin
from .models import Contestant, Profile, Quiz, Question, SubmittedAnswer, QuizCompletion


@admin.register(Contestant)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'points', 'is_admin']
    list_filter = ['user', 'points', 'is_admin']


@admin.register(Profile)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['contestant', 'social_link']
    list_filter = ['contestant']


@admin.register(Quiz)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image']
    list_filter = ['title']
    exclude = ('is_public',)


@admin.register(Question)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['quiz', 'title', 'time_limit']
    list_filter = ['quiz', 'title', 'time_limit']


@admin.register(SubmittedAnswer)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['question', 'user', 'chosen_answer']
    list_filter = ['question', 'user', 'chosen_answer']


@admin.register(QuizCompletion)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['quiz', 'contestant', 'completion_time', 'score']
    list_filter = ['quiz', 'contestant', 'completion_time', 'score']
