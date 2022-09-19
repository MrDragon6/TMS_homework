from django.http import HttpResponseBadRequest, HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Sum
from django.urls import reverse_lazy, reverse
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime


from . import models
from . import forms


def home(request):
    date_time = datetime.now()
    quiz_num = models.Quiz.objects.filter(is_public=True).count()
    contestant_num = models.Contestant.objects.all().count()
    points_sum = models.Contestant.objects.all().aggregate(Sum('points'))['points__sum']
    return render(request, 'home.html', {'date_time': date_time, 'quiz_num': quiz_num,
                                         'contestant_num': contestant_num, 'points_sum': points_sum})


@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'auth/login.html')

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            django_login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Please check your login/password!')
            return render(request, 'auth/login.html')

    return HttpResponseBadRequest('Error')


@csrf_exempt
def logout(request):
    if request.method == 'POST':
        django_logout(request)
        return redirect('home')
    return render(request, 'auth/logout.html')


@csrf_exempt
def signup(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'auth/signup.html')

    elif request.method == 'POST':
        data = request.POST.dict()
        if data.get('password') == data.get('password_repeat'):
            data.pop('csrfmiddlewaretoken')
            data.pop('password_repeat')
            password = data.pop('password')

            user: User = User.objects.create(**data)
            user.set_password(password)
            user.save()

            models.Contestant.objects.create(user=user)
            contestant = models.Contestant(user=user)
            contestant.save()

            models.Profile.objects.create(contestant=contestant)

            username = request.POST['username']
            email = request.POST['email']
            subject = 'Welcome to our Online Quiz site!'
            message = f'Dear {username}, we are glad you joined us! ' \
                      f'Challenge other contestants to get the best results!'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return render(request, 'auth/login.html')
        else:
            messages.warning(request, 'Your passwords don\'t match!')
            return redirect('/signup/')

    return HttpResponseBadRequest('Error')


def quiz_list(request):
    quiz_data = models.Quiz.objects.filter(is_public=True)
    return render(request, 'quiz/quiz_list.html', {'data': quiz_data})


class QuizInfoView(DetailView):
    model = models.Quiz
    template_name = 'quiz/quiz_info.html'

    def get_context_data(self, *args, **kwargs):
        context = super(QuizInfoView, self).get_context_data(*args, **kwargs)

        current_quiz = get_object_or_404(models.Quiz, id=self.kwargs['pk'])
        total_likes = current_quiz.total_likes()

        liked = False
        if current_quiz.likes.filter(pk=self.request.user.contestant.pk).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


def quiz_like(request, pk):
    quiz = get_object_or_404(models.Quiz, id=request.POST.get('quiz_id'))
    if quiz.likes.filter(pk=request.user.contestant.pk).exists():
        quiz.likes.remove(request.user.contestant)
    else:
        quiz.likes.add(request.user.contestant)

    return HttpResponseRedirect(reverse('quiz_info', args=[str(pk)]))


def quiz_questions(request, quiz_id):
    models.SubmittedAnswer.objects.filter(user=request.user.id).delete()
    quiz = models.Quiz.objects.get(id=quiz_id)
    question = models.Question.objects.filter(quiz=quiz).order_by('id').first()
    quest_number = 1

    return render(request, 'quiz/quiz_questions.html', {'question': question, 'quiz': quiz,
                                                        'quest_number': quest_number})


def submit_answer(request, quiz_id, question_id):
    score = 10
    quest_number = models.SubmittedAnswer.objects.filter(user=request.user).count() + 2

    if request.method == 'POST':
        quiz = models.Quiz.objects.get(id=quiz_id)
        question = models.Question.objects.filter(quiz=quiz, id__gt=question_id).exclude(id=question_id). \
            order_by('id').first()

        if 'skip' in request.POST:
            quest = models.Question.objects.get(id=question_id)
            user = request.user
            answer = 'No Answer :('
            models.SubmittedAnswer.objects.create(user=user, question=quest, chosen_answer=answer)
            if question:
                return render(request, 'quiz/quiz_questions.html', {'question': question, 'quiz': quiz,
                                                                    'quest_number': quest_number})
        else:
            quest = models.Question.objects.get(id=question_id)
            user = request.user
            answer = request.POST['answer']
            models.SubmittedAnswer.objects.create(user=user, question=quest, chosen_answer=answer)

        if question:
            return render(request, 'quiz/quiz_questions.html', {'question': question, 'quiz': quiz,
                                                                'quest_number': quest_number})
        else:
            result = models.SubmittedAnswer.objects.filter(user=request.user)
            skipped = models.SubmittedAnswer.objects.filter(user=request.user, chosen_answer='No Answer :(').count()
            attempted = models.SubmittedAnswer.objects.filter(user=request.user)\
                .exclude(chosen_answer='No Answer :(').count()

            right_answers_num = 0

            for row in result:
                if strip_tags(row.chosen_answer) == row.question.right_answer:
                    right_answers_num += 1
                    score += 2
                elif strip_tags(row.chosen_answer) != row.question.right_answer and row.chosen_answer != 'No Answer :(':
                    score -= 1

            percentage = round((right_answers_num*100)/result.count(), 2)

            if not models.QuizCompletion.objects.filter(quiz=quiz_id, contestant=request.user.contestant).exists():
                models.QuizCompletion.objects.create(quiz=quiz, contestant=request.user.contestant,
                                                     completion_time=datetime.now(), score=score)
                current_user = models.Contestant.objects.get(user=request.user)
                current_user.points += score
                current_user.save()
            return render(request, 'quiz/quiz_result.html',
                          {'result': result, 'total_skipped': skipped, 'attempted': attempted,
                           'right_answers_num': right_answers_num, 'percentage': percentage,
                           'score': score, 'quiz': quiz})
    else:
        return HttpResponse('Method not allowed!')


class ProfileView(DetailView):
    model = models.Profile
    template_name = 'profile/profile_view.html'

    def get_context_data(self, *args, **kwargs):

        page_user = get_object_or_404(models.Profile, id=self.kwargs['pk'])
        user_quiz_completion = models.QuizCompletion.objects.filter(contestant=page_user.contestant).order_by('id')

        context = {
            'page_user': page_user,
            'user_quiz_completion': user_quiz_completion
        }
        return context


class ProfileEditView(generic.UpdateView):
    model = models.Profile
    template_name = 'profile/profile_page_edit.html'
    fields = ['bio', 'profile_picture', 'social_link']
    success_url = reverse_lazy('home')


@csrf_exempt
def user_edit(request, user_id):
    user = get_object_or_404(User, pk=request.user.id)
    if request.method == "GET":
        form = forms.UserEditForm()
        return render(request, 'profile/edit_profile.html', {'form': form})
    elif request.method == "POST":
        form = forms.UserEditForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            user.save()
        return HttpResponseRedirect(reverse('home'))


@csrf_exempt
def password_edit(request: HttpRequest, user_id):
    if request.method == 'GET':
        return render(request, 'profile/password_edit.html')

    elif request.method == 'POST':
        data = request.POST.dict()

        if data.get('new_password') == data.get('new_password_repeat') \
                and check_password(data.get('old_password'), request.user.password):
            new_password = data.pop('new_password')

            request.user.set_password(new_password)
            request.user.save()
            return HttpResponseRedirect(reverse('home'))

        elif check_password(data.get('old_password'), request.user.password) is False:
            messages.warning(request, 'Wrong old password!')
            return HttpResponseRedirect(reverse('password_edit', args=[str(user_id)]))
        else:
            messages.warning(request, 'Your passwords don\'t match!')
            return HttpResponseRedirect(reverse('password_edit', args=[str(user_id)]))

    return HttpResponseBadRequest('Error')


def rules(request):
    return render(request, 'quiz/rules.html')


def leaderboard(request):
    contestants = models.Contestant.objects.order_by('-points')
    context = {
        'contestants': contestants,
    }
    return render(request, 'quiz/leaderboard.html', context=context)


def add_quiz(request):
    if request.user.is_authenticated:
        if request.user.contestant.is_admin:
            form = forms.QuizAddForm(initial={'is_public': False, 'likes': None, 'created_at': datetime.now})

            if request.method == 'POST':
                form = forms.QuizAddForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect('admin_panel')
            context = {'form': form}
            return render(request, 'admin/add_quiz.html', context)
        else:
            return redirect('admin_panel')
    else:
        return redirect('admin_panel')


class QuizEditView(generic.UpdateView):
    model = models.Quiz
    template_name = 'admin/edit_quiz.html'
    fields = ['title', 'description', 'image']
    success_url = reverse_lazy('admin_panel')


class QuestionEditView(generic.UpdateView):
    model = models.Question
    template_name = 'admin/edit_question.html'
    fields = ['title', 'image', 'answer_1', 'answer_2', 'answer_3', 'answer_4',
              'right_answer', 'time_limit']
    success_url = reverse_lazy('admin_panel')


def add_question(request, quiz_id):
    quiz = models.Quiz.objects.get(id=quiz_id)

    if request.user.is_authenticated:
        if request.user.contestant.is_admin:
            form = forms.QuestionAddForm(initial={'quiz': quiz_id})

            if request.method == 'POST':
                form = forms.QuestionAddForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect('admin_panel')
            context = {'form': form, 'quiz': quiz}
            return render(request, 'admin/add_question.html', context)
        else:
            return redirect('admin_panel')
    else:
        return redirect('admin_panel')


def list_questions(request, quiz_id):
    quiz = models.Quiz.objects.get(id=quiz_id)
    questions = models.Question.objects.filter(quiz=quiz_id).order_by('id')
    return render(request, 'admin/list_questions.html', {'questions': questions, 'quiz': quiz})


class QuizDeleteView(DeleteView):
    model = models.Quiz
    template_name = 'admin/delete_quiz.html'
    success_url = reverse_lazy('admin_panel')

    def get_context_data(self, *args, **kwargs):
        quiz_menu = models.Quiz.objects.all()
        context = super(QuizDeleteView, self).get_context_data(*args, **kwargs)
        context['quiz_menu'] = quiz_menu
        return context


class QuestionDeleteView(DeleteView):
    model = models.Question
    template_name = 'admin/delete_question.html'
    success_url = reverse_lazy('admin_panel')

    def get_context_data(self, *args, **kwargs):
        questions_menu = models.Question.objects.all()
        context = super(QuestionDeleteView, self).get_context_data(*args, **kwargs)
        context['question_menu'] = questions_menu
        return context


class AdminPanelView(ListView):
    model = models.Quiz
    template_name = 'admin/admin_panel.html'
    ordering = ['title']

    def get_context_data(self, *args, **kwargs):
        quiz_menu = models.Quiz.objects.all()
        context = super(AdminPanelView, self).get_context_data(*args, **kwargs)
        context['quiz_menu'] = quiz_menu
        return context


def quiz_switch_access(request, pk):
    quiz = get_object_or_404(models.Quiz, id=pk)

    if request.user.is_authenticated:
        if request.user.contestant.is_admin:
            if quiz.is_public is False:
                quiz.is_public = True
                quiz.save()
            else:
                quiz.is_public = False
                quiz.save()

            return redirect('admin_panel')
        else:
            return redirect('admin_panel')
    else:
        return redirect('admin_panel')
