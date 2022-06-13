from django.http import HttpResponseBadRequest, HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.urls import reverse_lazy

from .models import Reader, Post, Category
from .forms import PostForm, EditForm


@csrf_exempt
def home(request):
    return render(request, 'main/home.html')


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
            return render(request, 'auth/profile.html', context={'username': user.get_username()})
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
        data.pop('csrfmiddlewaretoken')
        password = data.pop('password')

        user: User = User.objects.create(**data)
        user.set_password(password)
        user.save()

        Reader.objects.create(user=user)

        reader = Reader(user=user)
        reader.save()

        return render(request, 'auth/login.html')

    return HttpResponseBadRequest('Error')


class HomeView(ListView):
    model = Post
    template_name = 'main/home.html'
    ordering = ['-creation_date']

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context


class PostView(DetailView):
    model = Post
    template_name = 'main/post_view.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(PostView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context


class PostAddView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'main/post_add.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(PostAddView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context


class PostUpdateView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'main/post_update.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(PostUpdateView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'main/post_delete.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(PostDeleteView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context


def category_list_view(request):
    category_menu_list = Category.objects.all()
    return render(request, 'main/category_list.html',
                  {'category_menu_list': category_menu_list})


def category_view(request, categories):
    category_posts = Post.objects.filter(category=categories.replace('-', ' '))
    return render(request, 'main/categories.html',
                  {'categories': categories.replace('-', ' ').title(), 'category_posts': category_posts})


class CategoryAddView(CreateView):
    model = Category
    template_name = 'main/category_add.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(CategoryAddView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context
