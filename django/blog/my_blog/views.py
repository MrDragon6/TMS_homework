from django.http import HttpResponseBadRequest, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth.hashers import check_password

from django.views import generic

from .models import Reader, Author, Post, Category, Profile, Comment, Subscription
from .forms import PostForm, EditForm, UserEditForm, CommentForm, ProfilePageForm


@csrf_exempt
def home(request):
    return render(request, 'home.html')


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

            Reader.objects.create(user=user)

            reader = Reader(user=user)
            reader.save()

            return render(request, 'auth/login.html')
        else:
            messages.warning(request, 'Your passwords don\'t match!')
            return redirect('/signup/')

    return HttpResponseBadRequest('Error')


@csrf_exempt
def user_edit(request, user_id):
    user = get_object_or_404(User, pk=request.user.id)
    if request.method == "GET":
        form = UserEditForm()
        return render(request, 'profile/edit_profile.html', {'form': form})
    elif request.method == "POST":
        form = UserEditForm(request.POST, instance=user)
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


@csrf_exempt
def create_author(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        Author.objects.create(user=user)
        author = Author(user=user)
        author.save()

        return redirect('home')
    return render(request, 'profile/create_author.html')


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_at']

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context


class ProfilePageCreateView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'profile/profile_page_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileView(DetailView):
    model = Profile
    template_name = 'profile/profile_view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(*args, **kwargs)

        user = get_object_or_404(User, id=self.request.user.id)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        subscribed = False
        if Subscription.objects.filter(subscriber_user=user, subscription_user=page_user.user).exists():
            subscribed = True

        total_subscribers = page_user.user.author.total_subscribers()

        context['page_user'] = page_user
        context['subscribed'] = subscribed
        context['total_subscribers'] = total_subscribers
        return context


class ProfileEditView(generic.UpdateView):
    model = Profile
    template_name = 'profile/profile_page_edit.html'
    fields = ['bio', 'profile_picture', 'website_url', 'facebook_url',
              'vkontakte_url', 'instagram_url']
    success_url = reverse_lazy('home')


class PostView(DetailView):
    model = Post
    template_name = 'post/post_view.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(PostView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['category_menu'] = category_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


class PostAddView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_add.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(PostAddView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context


class PostUpdateView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'post/post_update.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(PostUpdateView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(PostDeleteView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context


def category_list_view(request):
    category_menu_list = Category.objects.all()
    return render(request, 'category/category_list.html',
                  {'category_menu_list': category_menu_list})


def category_view(request, categories):
    category_posts = Post.objects.filter(category__name__contains=categories.replace('-', ' '))
    return render(request, 'category/categories.html',
                  {'categories': categories.replace('-', ' ').title(), 'category_posts': category_posts})


class CommentAddView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment/comment_add.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_view', kwargs={'pk': self.kwargs['pk']})


def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post_view', args=[str(pk)]))


def subscribe_view(request, pk):
    user_profile = get_object_or_404(User, id=request.POST.get('user_profile_id'))
    subscribed = False

    if Subscription.objects.filter(subscriber_user=request.user, subscription_user=user_profile).exists():
        Subscription.objects.filter(subscriber_user=request.user, subscription_user=user_profile).delete()
        user_profile.author.subscribers.remove(request.user)
    else:
        subscription = Subscription()
        subscription.save()

        subscription.subscription_user.add(user_profile)
        subscription.subscriber_user.add(request.user)

        subscription.save()
        user_profile.author.subscribers.add(request.user)
        subscribed = True

    return HttpResponseRedirect(reverse('view_profile', args=[str(user_profile.profile.pk)]))


def subscriptions_list_view(request):
    subscription_authors = Subscription.objects.filter(subscriber_user=request.user).values('subscription_user')
    subscription_authors_list = []
    subscription_posts = []

    for author in subscription_authors:
        subscription_authors_list.append(author.get('subscription_user'))

    for author in subscription_authors_list:
        for post in Post.objects.filter(author=author):
            subscription_posts.append(post)

    return render(request, 'subscriptions/subscriptions_list.html',
                  {'subscription_posts': subscription_posts})


